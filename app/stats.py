"""통계 엔진.

화면과 AI 에 나가는 숫자는 모두 여기서 계산합니다. AI 는 이 결과를 읽기만 합니다.

- 변화율: OLS 기울기 + 95% 신뢰구간, Sen 기울기 + 순위 기반 신뢰구간
- 유의성: 기울기 t-검정, Mann-Kendall (동점 보정 + 연속성 보정)
- 가산점: 잔차 1차 자기상관 보정 p값, 탐지 가능 연수(Weatherhead 1998 근사),
  가장 튄 해를 뺀 재검정, Benjamini-Hochberg FDR, 피어슨 상관
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional, Sequence

import numpy as np
from scipy import stats as sps

ALPHA = 0.05


# ---------------------------------------------------------------------------
# 기본 검정
# ---------------------------------------------------------------------------


def lag1_autocorr(x: Sequence[float]) -> float:
    """1차 자기상관 계수. 값이 거의 일정하면 0."""
    a = np.asarray(x, dtype=float)
    if a.size < 3:
        return 0.0
    a = a - a.mean()
    denom = float(np.dot(a, a))
    if denom == 0.0:
        return 0.0
    return float(np.dot(a[:-1], a[1:]) / denom)


def ols_trend(years: Sequence[float], values: Sequence[float], alpha: float = ALPHA) -> dict:
    """최소제곱 선형 추세. 기울기 단위는 '값/년'."""
    x = np.asarray(years, dtype=float)
    y = np.asarray(values, dtype=float)
    n = x.size
    if n < 3:
        raise ValueError("OLS trend needs at least 3 years")

    xm, ym = x.mean(), y.mean()
    sxx = float(np.sum((x - xm) ** 2))
    slope = float(np.sum((x - xm) * (y - ym)) / sxx)
    intercept = float(ym - slope * xm)
    resid = y - (intercept + slope * x)
    df = n - 2
    sse = float(np.sum(resid**2))
    se = math.sqrt(sse / df / sxx) if sse > 0 else 0.0

    if se == 0.0:
        t_stat = math.inf if slope != 0 else 0.0
        p = 0.0 if slope != 0 else 1.0
    else:
        t_stat = slope / se
        p = float(2 * sps.t.sf(abs(t_stat), df))

    tcrit = float(sps.t.ppf(1 - alpha / 2, df))

    # 잔차 1차 자기상관 보정: 유효 표본 수로 표준오차를 키웁니다.
    r1 = lag1_autocorr(resid)
    if r1 > 0:
        n_eff = n * (1 - r1) / (1 + r1)
    else:
        n_eff = float(n)
    n_eff = max(n_eff, 3.0)
    if se > 0 and n_eff < n:
        se_adj = se * math.sqrt((n - 2) / (n_eff - 2)) if n_eff > 2 else math.inf
        df_adj = max(n_eff - 2, 1.0)
        p_adj = float(2 * sps.t.sf(abs(slope / se_adj), df_adj)) if math.isfinite(se_adj) else 1.0
    else:
        se_adj, p_adj = se, p

    return {
        "slope": slope,
        "intercept": intercept,
        "se": se,
        "t": t_stat if math.isfinite(t_stat) else None,
        "df": df,
        "p": p,
        "ci_low": slope - tcrit * se,
        "ci_high": slope + tcrit * se,
        "resid_sd": math.sqrt(sse / df) if df > 0 else 0.0,
        "resid_lag1": r1,
        "n_eff": n_eff,
        "p_ar1": p_adj,
    }


def _mk_s_and_var(y: np.ndarray) -> tuple:
    n = y.size
    diff = y[None, :] - y[:, None]  # diff[i, j] = y[j] - y[i]
    iu = np.triu_indices(n, k=1)
    s = int(np.sign(diff[iu]).sum())
    _, counts = np.unique(y, return_counts=True)
    ties = counts[counts > 1]
    var_s = (n * (n - 1) * (2 * n + 5) - float(np.sum(ties * (ties - 1) * (2 * ties + 5)))) / 18.0
    return s, var_s


def mann_kendall(values: Sequence[float]) -> dict:
    """Mann-Kendall 단조 추세 검정 (양측, 정규 근사, 동점·연속성 보정)."""
    y = np.asarray(values, dtype=float)
    n = y.size
    if n < 4:
        raise ValueError("Mann-Kendall test needs at least 4 years")
    s, var_s = _mk_s_and_var(y)
    if var_s <= 0:
        z = 0.0
    elif s > 0:
        z = (s - 1) / math.sqrt(var_s)
    elif s < 0:
        z = (s + 1) / math.sqrt(var_s)
    else:
        z = 0.0
    p = float(2 * sps.norm.sf(abs(z)))
    tau = s / (n * (n - 1) / 2)
    return {"s": s, "var_s": var_s, "z": z, "p": p, "tau": tau}


def sen_slope(years: Sequence[float], values: Sequence[float], alpha: float = ALPHA) -> dict:
    """Theil-Sen 기울기와 Gilbert(1987) 순위 기반 신뢰구간."""
    x = np.asarray(years, dtype=float)
    y = np.asarray(values, dtype=float)
    n = x.size
    i, j = np.triu_indices(n, k=1)
    dx = x[j] - x[i]
    keep = dx != 0
    slopes = np.sort((y[j] - y[i])[keep] / dx[keep])
    slope = float(np.median(slopes))
    intercept = float(np.median(y - slope * x))

    _, var_s = _mk_s_and_var(y)
    big_n = slopes.size
    c = float(sps.norm.ppf(1 - alpha / 2)) * math.sqrt(max(var_s, 0.0))
    m1 = (big_n - c) / 2.0
    m2 = (big_n + c) / 2.0
    lo_idx = int(np.clip(round(m1) - 1, 0, big_n - 1))
    hi_idx = int(np.clip(round(m2), 0, big_n - 1))
    return {
        "slope": slope,
        "intercept": intercept,
        "ci_low": float(slopes[lo_idx]),
        "ci_high": float(slopes[hi_idx]),
    }


def detectable_years(slope_per_year: float, resid_sd: float, phi: float) -> Optional[float]:
    """Weatherhead et al. (1998) 근사: 현재 기울기가 유지될 때 유의해지는 데 필요한 총 관측 연수.

    n* ≈ [ (3.3 σ / |ω|) · sqrt((1+φ)/(1−φ)) ]^(2/3)
    (탐지력 90%, 유의수준 5% 기준의 근사식. 연 단위 자료에 그대로 적용합니다.)
    """
    if slope_per_year == 0 or not math.isfinite(slope_per_year) or resid_sd <= 0:
        return None
    phi = float(np.clip(phi, -0.9, 0.9))
    base = (3.3 * resid_sd / abs(slope_per_year)) * math.sqrt((1 + phi) / (1 - phi))
    return float(base ** (2.0 / 3.0))


def bh_fdr(pvals: Sequence[float]) -> list:
    """Benjamini-Hochberg q값."""
    p = np.asarray(pvals, dtype=float)
    m = p.size
    if m == 0:
        return []
    order = np.argsort(p)
    ranked = p[order] * m / (np.arange(m) + 1)
    q_sorted = np.minimum.accumulate(ranked[::-1])[::-1]
    q = np.empty(m)
    q[order] = np.clip(q_sorted, 0, 1)
    return [float(v) for v in q]


def pearson(x: Sequence[float], y: Sequence[float]) -> Optional[dict]:
    a = np.asarray(x, dtype=float)
    b = np.asarray(y, dtype=float)
    if a.size < 4 or np.std(a) == 0 or np.std(b) == 0:
        return None
    r, p = sps.pearsonr(a, b)
    return {"r": float(r), "p": float(p), "n": int(a.size)}


# ---------------------------------------------------------------------------
# 판정
# ---------------------------------------------------------------------------


@dataclass
class Verdict:
    status: str  # significant | mixed | not_significant
    direction: str  # increase | decrease | flat
    label: str

    def to_dict(self) -> dict:
        return {"status": self.status, "direction": self.direction, "label": self.label}


def make_verdict(p_t: float, p_mk: float, slope: float, alpha: float = ALPHA) -> Verdict:
    sig_t = p_t < alpha
    sig_mk = p_mk < alpha
    direction = "increase" if slope > 0 else "decrease" if slope < 0 else "flat"
    word = {"increase": "Increasing", "decrease": "Decreasing", "flat": "No change"}[direction]
    if sig_t and sig_mk:
        return Verdict("significant", direction, f"{word}, significant")
    if sig_t or sig_mk:
        return Verdict("mixed", direction, f"{word} trend, tests disagree")
    return Verdict("not_significant", direction, "Not significant")


def analyze_series(years: Sequence[int], values: Sequence[float], robust: bool = False) -> dict:
    """연도별 값 하나씩 → 변화율·유의성·신뢰구간·판정·인사이트 재료."""
    yrs = np.asarray(years, dtype=float)
    vals = np.asarray(values, dtype=float)
    n = int(yrs.size)
    if n < 5:
        raise ValueError("Trend analysis needs at least 5 years")

    ols = ols_trend(yrs, vals)
    mk = mann_kendall(vals)
    sen = sen_slope(yrs, vals)

    headline = sen if robust else ols
    method = "sen" if robust else "ols"
    verdict = make_verdict(ols["p"], mk["p"], headline["slope"] if headline["slope"] != 0 else ols["slope"])

    # 탐지 가능 연수 (유의하지 않거나 엇갈릴 때)
    # Sen 기울기가 0(날수 지표에서 흔함)이면 OLS 기울기로 근사합니다.
    det_slope = headline["slope"] if headline["slope"] != 0 else ols["slope"]
    n_star = detectable_years(det_slope, ols["resid_sd"], ols["resid_lag1"])
    detect = None
    if verdict.status != "significant":
        if n_star is None:
            # 기울기가 0 → 추정 불가
            detect = {"status": "no_trend", "total_years": None, "more_years": None}
        elif n_star <= n:
            # 이만한 기울기라면 지금 기간으로도 대개 잡혀야 함 → 실제 변화는 더 작거나 없을 수 있음
            detect = {"status": "length_enough", "total_years": round(n_star, 1), "more_years": None}
        else:
            detect = {
                "status": "need_more",
                "total_years": round(n_star, 1),
                "more_years": int(math.ceil(n_star - n)),
            }

    # 초기 10년 vs 최근 10년 (짧으면 절반씩)
    k = 10 if n >= 20 else n // 2
    early = {"from": int(yrs[0]), "to": int(yrs[k - 1]), "mean": float(vals[:k].mean())}
    late = {"from": int(yrs[-k]), "to": int(yrs[-1]), "mean": float(vals[-k:].mean())}

    # 극단값 상위 3개 연도 (평균에서 가장 먼 해)
    dev = vals - vals.mean()
    top = np.argsort(-np.abs(dev))[:3]
    extremes = [
        {"year": int(yrs[i]), "value": float(vals[i]), "anomaly": float(dev[i])} for i in sorted(top, key=lambda i: -abs(dev[i]))
    ]

    # 가장 튄 해(추세선에서 가장 먼 해)를 뺀 재검정
    resid = vals - (ols["intercept"] + ols["slope"] * yrs)
    worst = int(np.argmax(np.abs(resid)))
    mask = np.ones(n, dtype=bool)
    mask[worst] = False
    ols_wo = ols_trend(yrs[mask], vals[mask])
    mk_wo = mann_kendall(vals[mask])
    sen_wo = sen_slope(yrs[mask], vals[mask])
    head_wo = sen_wo if robust else ols_wo
    verdict_wo = make_verdict(ols_wo["p"], mk_wo["p"], head_wo["slope"] if head_wo["slope"] != 0 else ols_wo["slope"])
    leave_out = {
        "year": int(yrs[worst]),
        "value": float(vals[worst]),
        "p_t": ols_wo["p"],
        "p_mk": mk_wo["p"],
        "slope_per_decade": head_wo["slope"] * 10,
        "verdict": verdict_wo.to_dict(),
        "changes_verdict": verdict_wo.status != verdict.status or (
            verdict.status == "significant" and verdict_wo.direction != verdict.direction
        ),
    }

    flags = []
    if (ols["p"] < ALPHA) != (mk["p"] < ALPHA):
        flags.append("tests_disagree")
    if leave_out["changes_verdict"]:
        flags.append("one_year_drives_result")
    if ols["p"] < ALPHA <= ols["p_ar1"]:
        flags.append("autocorrelation_weakens")

    return {
        "n": n,
        "method": method,
        "slope_per_year": headline["slope"],
        "slope_per_decade": headline["slope"] * 10,
        "ci_per_decade": [headline["ci_low"] * 10, headline["ci_high"] * 10],
        "ols": {
            "slope_per_decade": ols["slope"] * 10,
            "ci_per_decade": [ols["ci_low"] * 10, ols["ci_high"] * 10],
            "intercept": ols["intercept"],
            "slope_per_year": ols["slope"],
            "t": ols["t"],
            "df": ols["df"],
            "p": ols["p"],
            "p_ar1": ols["p_ar1"],
            "resid_lag1": ols["resid_lag1"],
            "n_eff": ols["n_eff"],
        },
        "sen": {
            "slope_per_decade": sen["slope"] * 10,
            "ci_per_decade": [sen["ci_low"] * 10, sen["ci_high"] * 10],
            "intercept": sen["intercept"],
            "slope_per_year": sen["slope"],
        },
        "mk": {"s": mk["s"], "z": mk["z"], "p": mk["p"], "tau": mk["tau"]},
        "verdict": verdict.to_dict(),
        "detectable": detect,
        "early": early,
        "late": late,
        "extremes": extremes,
        "leave_out": leave_out,
        "flags": flags,
        "mean": float(vals.mean()),
        "resid_sd": ols["resid_sd"],
    }
