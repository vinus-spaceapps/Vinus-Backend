"""분석 요청 → 시계열·통계·판정 묶음, 그리고 인사이트 AI 에 넘길 재료."""

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Field

from . import catalog
from .series import SeriesUnavailable, get_series
from .stats import analyze_series, bh_fdr, pearson

RESOLUTION_NOTE = "Results are regional averages (tens of km) and do not represent a single vineyard."


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
    rate = f"{_fmt(st['slope_per_decade'])} {unit} per decade (95% CI {_fmt(lo)} to {_fmt(hi)})"
    body = f"{v['label']} · {rate} · Mann-Kendall p = {st['mk']['p']:.3f}"
    body += detect_sentence(st.get("detectable"), prefix=" · ")
    return f"{head}\n{body}"


def detect_sentence(det: Optional[dict], prefix: str = "") -> str:
    if not det:
        return ""
    if det["status"] == "need_more":
        return f"{prefix}if the current trend holds, about {det['more_years']} more years of data may be needed to reach significance (approx.)"
    if det["status"] == "length_enough":
        return f"{prefix}the record is already long enough, so the real change may be smaller than this slope, or none"
    return f"{prefix}the slope is close to zero, so years-to-detection cannot be estimated"


def _trend_points(years: list, intercept: float, slope: float) -> list:
    return [{"year": y, "value": round(intercept + slope * y, 3)} for y in (years[0], years[-1])]


def analyze_one(meta: dict, region_id: str, start: int, end: int, threshold=None) -> dict:
    try:
        s = get_series(meta, region_id, start, end, threshold)
    except SeriesUnavailable as e:
        raise AnalysisError(str(e)) from e
    if len(s.years) < 5:
        raise AnalysisError(f"{meta['name']}: only {len(s.years)} years can be analyzed (at least 5 needed).")
    st = analyze_series(s.years, s.values, robust=meta["robust"])
    return {"series": s, "stats": st}


def run_analysis(req: AnalyzeRequest) -> dict:
    region = catalog.region(req.region)
    if region is None:
        raise AnalysisError(f"Unknown region: {req.region}")
    if req.start >= req.end:
        raise AnalysisError("Start year must be before end year.")

    results = []
    for var_id in req.variables:
        meta = catalog.indicator(var_id)
        if meta is None:
            raise AnalysisError(f"Unknown indicator: {var_id}")
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
                "label": req.user_label or "My record",
                "points": [{"year": y, "value": user[y]} for y in sorted(user)],
                "correlation": corr,
                "common_years": len(common),
                "note": "Correlation is not causation. It only means the two moved together in the same years.",
            }

        notes = list(s.notes)
        if req.stages:
            notes.append("Your growth-stage dates will be used once daily-data aggregation is connected. Current values use the region's default dates.")

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
        parts.append(f"a mean minimum-temperature bias of {st['tmin_bias']:+.2f}°C (correlation {st['tmin_corr']:.2f})")
    if var in ("tmax", "tmean"):
        parts.append(f"a mean maximum-temperature bias of {st['tmax_bias']:+.2f}°C (correlation {st['tmax_corr']:.2f})")
    sentence = f"Compared with the nearby weather station ({st['id']}), the grid values show {' and '.join(parts)}."
    big = max(abs(st["tmin_bias"]) if var in ("tmin", "tmean") else 0, abs(st["tmax_bias"]) if var in ("tmax", "tmean") else 0)
    if big >= 2:
        sentence += " The bias is large, so focus on the direction of change rather than absolute values."
    modis = val.get("modis")
    if var == "tmin" and modis:
        sentence += f" At 1 km (MODIS satellite), night-time land surface temperature varies by {modis['pixel_spread_mean']:.1f}°C on average within the same grid cell."
    return {"station": st, "modis": modis if var == "tmin" else None, "sentence": sentence}


def build_materials(analysis: dict, var_id: str, context: Optional[dict] = None) -> dict:
    """인사이트 AI 입력: 엔진이 미리 계산한 재료 묶음. AI 는 여기 있는 숫자만 씁니다."""
    res = next((r for r in analysis["results"] if r["variable"]["id"] == var_id), None)
    if res is None:
        raise AnalysisError(f"Indicator not in this analysis: {var_id}")
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
            "method": "Sen slope" if st["method"] == "sen" else "OLS slope",
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
            {"id": f"{meta['id']}.md", "title": f"{meta['name']} indicator notes", "sections": meta["sections"]},
        ],
    }
