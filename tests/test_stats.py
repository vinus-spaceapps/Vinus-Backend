"""통계 엔진 검증: scipy 기준값과 비교 + 기획서의 5가지 판정 케이스."""

import numpy as np
import pytest
from scipy import stats as sps

from app.stats import analyze_series, bh_fdr, detectable_years, mann_kendall, ols_trend, sen_slope

YEARS = list(range(2003, 2026))


def test_ols_matches_scipy_linregress():
    rng = np.random.RandomState(0)
    y = 0.3 * np.arange(23) + rng.normal(0, 1, 23)
    ours = ols_trend(YEARS, y)
    ref = sps.linregress(YEARS, y)
    assert ours["slope"] == pytest.approx(ref.slope)
    assert ours["intercept"] == pytest.approx(ref.intercept)
    assert ours["se"] == pytest.approx(ref.stderr)
    assert ours["p"] == pytest.approx(ref.pvalue)
    tcrit = sps.t.ppf(0.975, 21)
    assert ours["ci_low"] == pytest.approx(ref.slope - tcrit * ref.stderr)


def test_sen_matches_scipy_theilslopes():
    rng = np.random.RandomState(1)
    y = 0.5 * np.arange(23) + rng.normal(0, 2, 23)
    ours = sen_slope(YEARS, y)
    ref = sps.theilslopes(y, YEARS)
    assert ours["slope"] == pytest.approx(ref.slope)
    assert ours["ci_low"] == pytest.approx(ref.low_slope)
    assert ours["ci_high"] == pytest.approx(ref.high_slope)


def test_mann_kendall_s_and_tau():
    y = [1, 3, 2, 5, 4, 6, 8, 7]
    mk = mann_kendall(y)
    # 손으로 센 S: 증가 쌍 25, 감소 쌍 3
    assert mk["s"] == 22
    tau, _ = sps.kendalltau(range(len(y)), y)
    assert mk["tau"] == pytest.approx(tau)
    # 동점 없음: var = n(n-1)(2n+5)/18
    n = len(y)
    assert mk["var_s"] == pytest.approx(n * (n - 1) * (2 * n + 5) / 18)
    z = (22 - 1) / np.sqrt(mk["var_s"])
    assert mk["p"] == pytest.approx(2 * sps.norm.sf(z))


def test_mann_kendall_tie_correction():
    y = [0, 0, 1, 1, 1, 2, 3, 3]
    mk = mann_kendall(y)
    n = 8
    ties = np.array([2, 3, 2])
    expected = (n * (n - 1) * (2 * n + 5) - np.sum(ties * (ties - 1) * (2 * ties + 5))) / 18
    assert mk["var_s"] == pytest.approx(expected)


def test_bh_fdr_matches_reference():
    p = [0.01, 0.04, 0.03, 0.20]
    q = bh_fdr(p)
    assert q == pytest.approx([0.04, 0.16 / 3, 0.16 / 3, 0.2])
    assert q == pytest.approx(list(sps.false_discovery_control(p, method="bh")))


def test_detectable_years_formula():
    n = detectable_years(0.1, 1.0, 0.0)
    assert n == pytest.approx((3.3 * 1.0 / 0.1) ** (2 / 3))
    assert detectable_years(0.0, 1.0, 0.0) is None


# --- 기획서 5장 테스트 케이스 -------------------------------------------------


def test_case1_significant_increase():
    rng = np.random.RandomState(2)
    y = 2 + 0.4 * np.arange(23) + rng.normal(0, 1, 23)
    r = analyze_series(YEARS, y)
    assert r["verdict"]["status"] == "significant"
    assert r["verdict"]["direction"] == "increase"
    assert r["verdict"]["label"] == "증가, 유의함"
    assert r["detectable"] is None
    assert r["ci_per_decade"][0] > 0


def test_case2_significant_decrease():
    rng = np.random.RandomState(3)
    y = 10 - 0.3 * np.arange(23) + rng.normal(0, 1, 23)
    r = analyze_series(YEARS, y)
    assert r["verdict"]["label"] == "감소, 유의함"
    assert r["ci_per_decade"][1] < 0


def test_case3_not_significant_reports_detectable_years():
    rng = np.random.RandomState(4)
    y = 5 + 0.02 * np.arange(23) + rng.normal(0, 2, 23)
    r = analyze_series(YEARS, y)
    assert r["verdict"]["status"] == "not_significant"
    assert r["detectable"] is not None
    assert r["detectable"]["status"] in {"need_more", "length_enough", "no_trend"}
    if r["detectable"]["status"] == "need_more":
        assert r["detectable"]["more_years"] > 0


def test_case4_ttest_significant_but_mk_not():
    # 거의 평평하다가 마지막 몇 해가 크게 튐 → OLS 기울기는 유의, 순위 검정은 아님
    y = np.array([3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 12, 3, 14], dtype=float)
    r = analyze_series(YEARS, y)
    assert r["ols"]["p"] < 0.05
    assert r["mk"]["p"] >= 0.05
    assert r["verdict"]["status"] == "mixed"
    assert "tests_disagree" in r["flags"]


def test_case5_dropping_2020_changes_verdict():
    rng = np.random.RandomState(5)
    y = 2 + 0.06 * np.arange(23) + rng.normal(0, 0.8, 23)
    y[YEARS.index(2020)] += 15
    r = analyze_series(YEARS, y, robust=False)
    assert r["leave_out"]["year"] == 2020
    if r["verdict"]["status"] != r["leave_out"]["verdict"]["status"]:
        assert r["leave_out"]["changes_verdict"]
        assert "one_year_drives_result" in r["flags"]


def test_case5_mock_yeongdong_rain_flags_one_year():
    from app.analysis import AnalyzeRequest, run_analysis

    a = run_analysis(AnalyzeRequest(variables=["harvest_rain_days"], region="yeongdong", start=2003, end=2025))
    st = a["results"][0]["stats"]
    assert st["verdict"]["status"] == "significant"
    assert "one_year_drives_result" in st["flags"]


def test_robust_uses_sen_headline():
    y = np.array([0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2, 0, 1, 0, 9, 11, 1, 17, 7, 4, 2, 5, 3], dtype=float)
    r = analyze_series(YEARS, y, robust=True)
    assert r["method"] == "sen"
    assert r["slope_per_decade"] == pytest.approx(r["sen"]["slope_per_decade"])
