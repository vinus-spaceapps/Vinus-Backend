"""분석 요청 → 시계열·통계·판정 묶음, 그리고 인사이트 AI 에 넘길 재료."""

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from . import catalog
from .series import SeriesUnavailable, get_series
from .stats import analyze_series, bh_fdr, pearson

RESOLUTION_NOTE = "결과는 산지 단위(수십 km) 평균이며 밭 하나를 대표하지 않습니다."


class YearValue(BaseModel):
    year: int
    value: float


class AnalyzeRequest(BaseModel):
    variables: List[str] = Field(..., min_length=1, max_length=3)
    region: str
    start: int = 2001
    end: int = 2026
    thresholds: Dict[str, float] = Field(default_factory=dict)
    stages: Optional[Dict[str, str]] = None
    user_series: Optional[List[YearValue]] = None
    user_label: Optional[str] = None


class AnalysisError(ValueError):
    pass


def _fmt(x: float, digits: int = 1) -> str:
    s = f"{x:+.{digits}f}"
    return s.replace("+-", "-")


def _verdict_sentence(meta: dict, region: dict, start: int, end: int, st: dict) -> str:
    unit = meta.get("unit", "")
    v = st["verdict"]
    lo, hi = st["ci_per_decade"]
    head = f"{region['name']} · {meta['name']} · {start}~{end}"
    rate = f"10년에 {_fmt(st['slope_per_decade'])}{unit} (95% 신뢰구간 {_fmt(lo)} ~ {_fmt(hi)})"
    body = f"{v['label']} · {rate} · Mann-Kendall p = {st['mk']['p']:.3f}"
    body += detect_sentence(st.get("detectable"), prefix=" · ")
    return f"{head}\n{body}"


def detect_sentence(det: Optional[dict], prefix: str = "") -> str:
    if not det:
        return ""
    if det["status"] == "need_more":
        return f"{prefix}현재 추세가 유지되면 약 {det['more_years']}년 더 관측해야 유의해질 수 있음(근사)"
    if det["status"] == "length_enough":
        return f"{prefix}관측 기간은 충분한 편이라, 실제 변화는 지금 기울기보다 작거나 없을 수 있음"
    return f"{prefix}기울기가 0에 가까워 탐지 가능 연수를 추정할 수 없음"


def _trend_points(years: list, intercept: float, slope: float) -> list:
    return [{"year": y, "value": round(intercept + slope * y, 3)} for y in (years[0], years[-1])]


def analyze_one(meta: dict, region_id: str, start: int, end: int, threshold=None) -> dict:
    try:
        s = get_series(meta, region_id, start, end, threshold)
    except SeriesUnavailable as e:
        raise AnalysisError(str(e)) from e
    if len(s.years) < 5:
        raise AnalysisError(f"{meta['name']}: 분석 가능한 연도가 {len(s.years)}개뿐입니다 (5개 이상 필요).")
    st = analyze_series(s.years, s.values, robust=meta["robust"])
    return {"series": s, "stats": st}


def run_analysis(req: AnalyzeRequest) -> dict:
    region = catalog.region(req.region)
    if region is None:
        raise AnalysisError(f"알 수 없는 산지입니다: {req.region}")
    if req.start >= req.end:
        raise AnalysisError("시작 연도는 끝 연도보다 앞서야 합니다.")

    results = []
    for var_id in req.variables:
        meta = catalog.indicator(var_id)
        if meta is None:
            raise AnalysisError(f"알 수 없는 변수입니다: {var_id}")
        thr = req.thresholds.get(var_id, meta.get("threshold"))
        main = analyze_one(meta, region["id"], req.start, req.end, thr)
        s, st = main["series"], main["stats"]

        # 다른 산지 비교 (지도 색 + FDR)
        comp = []
        for r in catalog.regions():
            try:
                o = main if r["id"] == region["id"] else analyze_one(meta, r["id"], req.start, req.end, thr)
            except AnalysisError:
                continue
            ost = o["stats"]
            comp.append(
                {
                    "region_id": r["id"],
                    "name": r["name"],
                    "lat": r["lat"],
                    "lon": r["lon"],
                    "status": ost["verdict"]["status"],
                    "direction": ost["verdict"]["direction"],
                    "label": ost["verdict"]["label"],
                    "slope_per_decade": ost["slope_per_decade"],
                    "p_t": ost["ols"]["p"],
                    "p_mk": ost["mk"]["p"],
                    "is_mock": o["series"].is_mock,
                }
            )
        qs = bh_fdr([c["p_mk"] for c in comp])
        for c, q in zip(comp, qs):
            c["q_mk"] = q

        overlay = None
        if req.user_series:
            user = {p.year: p.value for p in req.user_series}
            common = [y for y in s.years if y in user]
            mine = {y: v for y, v in zip(s.years, s.values)}
            corr = pearson([mine[y] for y in common], [user[y] for y in common]) if len(common) >= 4 else None
            overlay = {
                "label": req.user_label or "내 기록",
                "points": [{"year": y, "value": user[y]} for y in sorted(user)],
                "correlation": corr,
                "common_years": len(common),
                "note": "상관은 인과가 아닙니다. 같은 해에 같이 움직였다는 뜻일 뿐입니다.",
            }

        notes = list(s.notes)
        if req.stages:
            notes.append("입력한 생육 단계 날짜는 실제 일별 데이터 집계를 연결하면 반영됩니다. 지금 값은 산지 기본 날짜 기준입니다.")

        results.append(
            {
                "variable": catalog.public_indicator(meta),
                "threshold": thr,
                "series": [{"year": y, "value": v} for y, v in zip(s.years, s.values)],
                "trend": {
                    "ols": _trend_points(s.years, st["ols"]["intercept"], st["ols"]["slope_per_year"]),
                    "sen": _trend_points(s.years, st["sen"]["intercept"], st["sen"]["slope_per_year"]),
                },
                "stats": st,
                "start": s.years[0],
                "end": s.years[-1],
                "is_mock": s.is_mock,
                "source_note": s.source_note,
                "notes": notes,
                "verdict_text": _verdict_sentence(meta, region, s.years[0], s.years[-1], st),
                "regions": comp,
                "overlay": overlay,
            }
        )

    return {
        "region": region,
        "start": req.start,
        "end": req.end,
        "stages": req.stages or region["stages"],
        "resolution_note": RESOLUTION_NOTE,
        "validation": catalog.validation(region["id"]),
        "is_mock": any(r["is_mock"] for r in results),
        "results": results,
    }


def ground_check(meta: dict, val: Optional[dict]) -> Optional[dict]:
    """지표가 쓰는 기온과 같은 종류로, 근처 지상 관측소·MODIS 1km 비교 결과를 한 문장으로."""
    var = meta.get("station_var")
    if not var or not val or "station" not in val:
        return None
    st = val["station"]
    parts = []
    if var in ("tmin", "tmean"):
        parts.append(f"최저기온 평균 오차 {st['tmin_bias']:+.2f}°C(상관 {st['tmin_corr']:.2f})")
    if var in ("tmax", "tmean"):
        parts.append(f"최고기온 평균 오차 {st['tmax_bias']:+.2f}°C(상관 {st['tmax_corr']:.2f})")
    sentence = f"근처 지상 관측소({st['id']})와 비교하면 격자 값은 {', '.join(parts)}입니다."
    big = max(abs(st["tmin_bias"]) if var in ("tmin", "tmean") else 0, abs(st["tmax_bias"]) if var in ("tmax", "tmean") else 0)
    if big >= 2:
        sentence += " 오차가 커서 절대값보다 변화 방향 위주로 보는 것이 좋습니다."
    modis = val.get("modis")
    if var == "tmin" and modis:
        sentence += f" 1km 위성(MODIS)으로 보면 같은 격자 안에서도 밤 지표면 온도가 평균 {modis['pixel_spread_mean']:.1f}°C 차이 납니다."
    return {"station": st, "modis": modis if var == "tmin" else None, "sentence": sentence}


def build_materials(analysis: dict, var_id: str, context: Optional[dict] = None) -> dict:
    """인사이트 AI 입력: 엔진이 미리 계산한 재료 묶음. AI 는 여기 있는 숫자만 씁니다."""
    res = next((r for r in analysis["results"] if r["variable"]["id"] == var_id), None)
    if res is None:
        raise AnalysisError(f"분석 결과에 없는 변수입니다: {var_id}")
    meta = catalog.indicator(var_id)
    st = res["stats"]
    region = analysis["region"]
    near = catalog.nearest_region(region["id"])
    others = [
        {k: c[k] for k in ("region_id", "name", "label", "slope_per_decade", "p_mk", "q_mk")}
        for c in res["regions"]
        if c["region_id"] != region["id"]
    ]
    r4 = lambda x: None if x is None else round(float(x), 4)  # noqa: E731
    # p값은 아주 작을 때 0.0 으로 뭉개지지 않도록 유효숫자 2자리
    rp = lambda x: None if x is None else (float(f"{float(x):.2g}") if float(x) < 0.001 else round(float(x), 4))  # noqa: E731
    return {
        "indicator": {
            "id": meta["id"],
            "name": meta["name"],
            "unit": meta.get("unit", ""),
            "short": meta.get("short", ""),
            "dataset": meta.get("dataset", ""),
            "source": meta.get("source", ""),
            "stage": meta.get("stage", ""),
            "condition": meta.get("condition", ""),
            "threshold": res["threshold"],
            "threshold_unit": meta.get("threshold_unit") or "",
            "threshold_options": meta["threshold_options"],
            "higher_is": meta.get("higher_is", "neutral"),
            "resolution": meta.get("resolution", ""),
            "start_year_available": meta["start_year"],
        },
        "region": {"id": region["id"], "name": region["name"], "country": region["country"]},
        "nearest_region": {"id": near["id"], "name": near["name"]} if near else None,
        "period": {"start": res["start"], "end": res["end"], "n_years": st["n"]},
        "selected_variables": [r["variable"]["id"] for r in analysis["results"]],
        "data_is_mock": res["is_mock"],
        "ground_check": ground_check(meta, analysis.get("validation")),
        "resolution_note": analysis["resolution_note"],
        "trend": {
            "method": "Sen 기울기" if st["method"] == "sen" else "OLS 기울기",
            "slope_per_decade": r4(st["slope_per_decade"]),
            "ci95_per_decade": [r4(st["ci_per_decade"][0]), r4(st["ci_per_decade"][1])],
            "ols_slope_per_decade": r4(st["ols"]["slope_per_decade"]),
            "sen_slope_per_decade": r4(st["sen"]["slope_per_decade"]),
            "p_ttest": rp(st["ols"]["p"]),
            "p_mann_kendall": rp(st["mk"]["p"]),
            "p_ttest_autocorr_adjusted": rp(st["ols"]["p_ar1"]),
            "verdict": st["verdict"],
            "detectable": st["detectable"],
        },
        "early_vs_late": {
            "early": {**st["early"], "mean": r4(st["early"]["mean"])},
            "late": {**st["late"], "mean": r4(st["late"]["mean"])},
            "difference": r4(st["late"]["mean"] - st["early"]["mean"]),
        },
        "extremes": [{**e, "value": r4(e["value"]), "anomaly": r4(e["anomaly"])} for e in st["extremes"]],
        "leave_out_most_extreme": {
            **st["leave_out"],
            "p_t": rp(st["leave_out"]["p_t"]),
            "p_mk": rp(st["leave_out"]["p_mk"]),
            "slope_per_decade": r4(st["leave_out"]["slope_per_decade"]),
        },
        "flags": st["flags"],
        "other_regions": [{**o, "slope_per_decade": r4(o["slope_per_decade"]), "p_mk": rp(o["p_mk"]), "q_mk": rp(o["q_mk"])} for o in others],
        "user_record": (
            {
                "label": res["overlay"]["label"],
                "correlation": res["overlay"]["correlation"],
                "common_years": res["overlay"]["common_years"],
            }
            if res["overlay"]
            else None
        ),
        "user_context": context or {},
        "documents": [
            {"id": f"{meta['id']}.md", "title": f"{meta['name']} 지표 문서", "sections": meta["sections"]},
        ],
    }
