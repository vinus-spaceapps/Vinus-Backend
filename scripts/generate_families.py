"""일별 원자료 → 체계적으로 만든 지표 묶음 (import_team_xlsx.py 가 불러 씁니다).

묶음
- stats    : 월·계절 기본 통계 (변수 × 기간 × 통계)
- extremes : 평년(2001~2010) 대비 극값 일수 (기간 × 지수)
- etccdi   : 세계기상기구 기후변화 탐지 지수(ETCCDI) 27개, 시즌 1년 기준

남반구는 같은 생육 단계끼리 비교되도록 달을 6개월 밀어 맞춥니다
(북반구 4월 발아 ↔ 남반구 10월, 북반구 9월 수확 ↔ 남반구 3월). 시즌 연도는 수확 연도입니다.
"""

from __future__ import annotations

import calendar
import math
from datetime import date, timedelta

import numpy as np

FIRST, LAST_YEAR = 2001, 2026
COVERAGE = 0.95
BASE_YEARS = range(2001, 2011)

# ---------------------------------------------------------------------------
# 변수
# ---------------------------------------------------------------------------
# key: (이름, 단위, 카테고리, 쓰는 통계, 생산자 의미, 주의점, 관측소 비교)
VARS = {
    "t2m": ("mean temperature", "°C", "temp_frost", ("mean", "min", "max"), "The basic temperature that sets how fast vines grow and ripen.", "A ~50 km grid average, so elevation and slope differences are not captured.", "tmean"),
    "tmin": ("minimum temperature", "°C", "temp_frost", ("mean", "min", "max"), "Night-time temperature. It drives frost and cold damage and how well acidity and color are kept.", "Cold-air pooling on valley floors is poorly captured by a ~50 km grid.", "tmin"),
    "tmax": ("maximum temperature", "°C", "heat", ("mean", "min", "max"), "Daytime temperature. It affects photosynthesis, sunburn and acid loss.", "A ~50 km grid average, so slope aspect differences are not captured.", "tmax"),
    "dtr": ("diurnal temperature range", "°C", "growth", ("mean", "min", "max"), "The day–night temperature difference. A larger range helps keep color, aroma and acidity.", "Grid averages understate the real range in valleys and on hillsides.", "tmean"),
    "prec": ("precipitation", "mm", "rain_water", ("sum", "max", "wet"), "The water supply, and a driver of disease and berry splitting.", "MERRA-2 precipitation is a model blended with observations, so local showers can be underestimated.", None),
    "rh": ("relative humidity", "%", "disease", ("mean", "min", "max"), "Affects fungal disease risk and how much water leaves lose (transpiration).", "Daily means miss night dew and midday dryness.", None),
    "qv": ("specific humidity", "g/kg", "disease", ("mean", "min", "max"), "Grams of water vapor per kg of air — how muggy it is.", "Daily means.", None),
    "vpd": ("vapor pressure deficit (VPD)", "kPa", "drought", ("mean", "min", "max"), "How strongly the air pulls water from leaves. Higher means more water stress.", "Computed from daily mean temperature and humidity, so it is lower than midday values.", None),
    "et0": ("reference evapotranspiration", "mm", "drought", ("sum", "max"), "Water lost from soil and leaves to evaporation — the irrigation demand.", "The Hargreaves formula uses only temperature and latitude, so wind and humidity effects are left out.", None),
    "gwtop": ("topsoil moisture", "0–1", "drought", ("mean", "min", "max"), "How wet the topsoil is (0 = dry, 1 = saturated). It shows short dry spells first.", "Model values; they differ from irrigated vineyards.", None),
    "gwroot": ("root-zone soil moisture", "0–1", "drought", ("mean", "min", "max"), "How wet the deeper soil that roots use is. It shows drought stress.", "Model values; they differ from irrigated vineyards.", None),
    "solar": ("solar radiation", "MJ/m²/day", "sun_wind", ("mean", "min", "max"), "Sunlight that powers photosynthesis and builds sugar and color. Too much causes sunburn.", "CERES satellite 1° grid values; the last few days are not yet available.", None),
    "wind": ("wind speed", "m/s", "sun_wind", ("mean", "min", "max"), "Airflow reduces disease, but strong wind breaks shoots and dries vines; calm nights favor radiation frost.", "Daily mean wind at 2 m, so gusts are not captured.", None),
}
POWER_COL = {"t2m": "T2M", "tmin": "T2M_MIN", "tmax": "T2M_MAX", "prec": "PRECTOTCORR", "rh": "RH2M", "qv": "QV2M",
             "gwtop": "GWETTOP", "gwroot": "GWETROOT", "solar": "ALLSKY_SFC_SW_DWN", "wind": "WS2M"}
STAT_LABEL = {"mean": "mean", "min": "minimum", "max": "maximum", "sum": "total", "wet": "rainy days"}

# ---------------------------------------------------------------------------
# 기간 (북반구 달 기준, 남반구는 6개월 밀어 맞춤)
# ---------------------------------------------------------------------------
MONTH_NAME = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
MONTH_STAGE = {1: "deep dormancy", 2: "late dormancy", 3: "pre-budburst", 4: "budburst", 5: "shoot growth", 6: "flowering", 7: "fruit set & berry growth",
               8: "veraison", 9: "ripening & harvest", 10: "end of harvest", 11: "leaf fall", 12: "dormancy"}
# key: (이름, [(북반구 달, 연도 오프셋)], 의미)
WINDOWS = {f"m{m:02d}": (f"{MONTH_NAME[m]} ({MONTH_STAGE[m]})", [(m, 0)], f"{MONTH_NAME[m]} in the Northern Hemisphere ({MONTH_NAME[(m + 5) % 12 + 1]} in the Southern), the vine's {MONTH_STAGE[m]} stage.") for m in range(1, 13)}
WINDOWS.update({
    "winter": ("Winter (Dec–Feb)", [(12, -1), (1, 0), (2, 0)], "Midwinter, when vines rest (Jun–Aug in the Southern Hemisphere)."),
    "spring": ("Spring (Mar–May)", [(3, 0), (4, 0), (5, 0)], "When buds break and shoots grow (Sep–Nov in the Southern Hemisphere)."),
    "summer": ("Summer (Jun–Aug)", [(6, 0), (7, 0), (8, 0)], "Flowering, berry growth and veraison (Dec–Feb in the Southern Hemisphere)."),
    "autumn": ("Autumn (Sep–Nov)", [(9, 0), (10, 0), (11, 0)], "Ripening, harvest and cane hardening (Mar–May in the Southern Hemisphere)."),
    "gs": ("Growing season (Apr–Oct)", [(m, 0) for m in range(4, 11)], "The whole growing season from budburst to harvest (Oct–Apr in the Southern Hemisphere)."),
    "harvest": ("Harvest period (Aug–Sep)", [(8, 0), (9, 0)], "The last two months of ripening (Feb–Mar in the Southern Hemisphere)."),
    "dormancy": ("Dormancy (Nov–Mar)", [(11, -1), (12, -1), (1, 0), (2, 0), (3, 0)], "From leaf fall until the next budburst (May–Sep in the Southern Hemisphere)."),
    "year": ("Season year (Oct–Sep)", [(m, -1) for m in (10, 11, 12)] + [(m, 0) for m in range(1, 10)], "The season year from the month after harvest to the next harvest (Apr–Mar in the Southern Hemisphere)."),
})


def window_dates(key: str, y: int, south: bool):
    months = WINDOWS[key][1]
    spans = []
    for m, off in months:
        yy = y + off
        if south:
            cm = (m + 5) % 12 + 1
            cy = yy if m >= 7 else yy - 1
        else:
            cm, cy = m, yy
        spans.append((date(cy, cm, 1), date(cy, cm, calendar.monthrange(cy, cm)[1])))
    return spans[0][0], spans[-1][1]


# 핵심 지표와 정의가 같은 조합은 만들지 않습니다.
DUPLICATES = {
    ("t2m", "gs", "mean"), ("t2m", "harvest", "mean"), ("t2m", "winter", "mean"), ("t2m", "spring", "mean"), ("t2m", "m06", "mean"),
    ("t2m", "m07", "mean"), ("tmin", "m09", "mean"), ("tmin", "gs", "mean"), ("tmin", "harvest", "mean"), ("tmin", "winter", "min"),
    ("tmax", "gs", "mean"), ("tmax", "harvest", "mean"), ("tmax", "gs", "max"), ("dtr", "gs", "mean"), ("dtr", "harvest", "mean"),
    ("prec", "harvest", "sum"), ("prec", "gs", "sum"), ("prec", "dormancy", "sum"), ("prec", "year", "sum"), ("prec", "gs", "max"),
    ("prec", "harvest", "max"), ("prec", "harvest", "wet"), ("prec", "gs", "wet"), ("prec", "m06", "sum"), ("prec", "m06", "wet"),
    ("prec", "m07", "sum"), ("rh", "harvest", "mean"), ("rh", "gs", "mean"), ("vpd", "gs", "mean"), ("et0", "gs", "sum"),
    ("gwtop", "gs", "mean"), ("gwroot", "gs", "mean"), ("gwroot", "harvest", "mean"), ("solar", "gs", "mean"), ("solar", "harvest", "mean"),
    ("solar", "m06", "mean"), ("solar", "m07", "mean"), ("wind", "gs", "mean"),
}

# ---------------------------------------------------------------------------
# 일별 배열
# ---------------------------------------------------------------------------


def _ra(lat_deg: float, doy: np.ndarray) -> np.ndarray:
    phi = math.radians(lat_deg)
    dr = 1 + 0.033 * np.cos(2 * np.pi * doy / 365)
    dec = 0.409 * np.sin(2 * np.pi * doy / 365 - 1.39)
    ws = np.arccos(np.clip(-math.tan(phi) * np.tan(dec), -1, 1))
    return 24 * 60 / np.pi * 0.0820 * dr * (ws * math.sin(phi) * np.sin(dec) + math.cos(phi) * np.cos(dec) * np.sin(ws))


class Daily:
    def __init__(self, records: dict, lat: float):
        self.d0 = min(records)
        n = (max(records) - self.d0).days + 1
        self.arr = {}
        for k, col in POWER_COL.items():
            a = np.full(n, np.nan)
            for d, rec in records.items():
                v = rec.get(col)
                if v is not None:
                    a[(d - self.d0).days] = v
            self.arr[k] = a
        t, tx, tn, rh = self.arr["t2m"], self.arr["tmax"], self.arr["tmin"], self.arr["rh"]
        self.arr["dtr"] = tx - tn
        es = 0.6108 * np.exp(17.27 * t / (t + 237.3))
        self.arr["vpd"] = es * (1 - rh / 100)
        doy = np.array([(self.d0 + timedelta(days=i)).timetuple().tm_yday for i in range(n)], dtype=float)
        self.arr["et0"] = 0.0023 * (t + 17.8) * np.sqrt(np.clip(tx - tn, 0, None)) * 0.408 * _ra(lat, doy)
        self.n = n

    def slice(self, key: str, start: date, end: date):
        """기간 값. 95% 미만이면 None."""
        i, j = (start - self.d0).days, (end - self.d0).days + 1
        if i < 0 or j > self.n:
            want = (end - start).days + 1
            i2, j2 = max(i, 0), min(j, self.n)
            a = self.arr[key][i2:j2] if j2 > i2 else np.array([])
        else:
            want = j - i
            a = self.arr[key][i:j]
        if want <= 0 or np.count_nonzero(~np.isnan(a)) < COVERAGE * want:
            return None
        return a[~np.isnan(a)]


def _stat(a: np.ndarray, stat: str):
    if stat == "mean":
        return float(a.mean())
    if stat == "min":
        return float(a.min())
    if stat == "max":
        return float(a.max())
    if stat == "sum":
        return float(a.sum())
    if stat == "wet":
        return int((a >= 1).sum())
    raise ValueError(stat)


def _longest(mask: np.ndarray) -> int:
    best = cur = 0
    for v in mask:
        cur = cur + 1 if v else 0
        best = max(best, cur)
    return best


def _spell_days(mask: np.ndarray, n: int = 6) -> int:
    """n일 이상 이어진 구간에 속한 날의 수 (WSDI·CSDI)."""
    total = cur = 0
    for v in list(mask) + [False]:
        if v:
            cur += 1
        else:
            if cur >= n:
                total += cur
            cur = 0
    return total


def _r(v, d=2):
    return None if v is None else round(v, d)


# ---------------------------------------------------------------------------
# 묶음 계산
# ---------------------------------------------------------------------------


def build(daily_by_region: dict, south_by_region: dict, lat_by_region: dict):
    """반환: (메타데이터 목록, {산지: {지표id: {연도: 값}}})"""
    D = {r: Daily(recs, lat_by_region[r]) for r, recs in daily_by_region.items()}
    metas: list = []
    values: dict = {r: {} for r in D}

    def put(rid, vid, y, v):
        if v is not None and not (isinstance(v, float) and math.isnan(v)):
            values[rid].setdefault(vid, {})[y] = v

    # ---- 1) 월·계절 기본 통계
    order = 0
    for vkey, (vname, unit, cat, stats, meaning, caveat, station) in VARS.items():
        for wkey, (wname, _, wmean) in WINDOWS.items():
            for stat in stats:
                if (vkey, wkey, stat) in DUPLICATES:
                    continue
                vid = f"{'m' if wkey.startswith('m') and wkey[1:].isdigit() else 's'}_{wkey.lstrip('m') if wkey[1:].isdigit() else wkey}_{vkey}_{stat}"
                order += 1
                if stat == "wet":
                    name, u, agg, cond = f"{wname} rainy days", "days", "count", "daily precipitation ≥ 1 mm"
                elif stat == "sum":
                    name, u, agg, cond = f"{wname} total {vname}", unit, "sum", "(no condition) period total"
                elif stat == "mean":
                    name, u, agg, cond = f"{wname} mean {vname}", unit, "mean", "(no condition) period mean"
                else:
                    name, u, agg, cond = f"{wname} {STAT_LABEL[stat]} {vname}", unit, stat, f"(no condition) {STAT_LABEL[stat]} daily {vname} in the period"
                desc = {"mean": f"the average daily {vname}", "min": f"the lowest daily {vname}", "max": f"the highest daily {vname}",
                        "sum": f"the sum of daily {vname}", "wet": "the number of days with at least 1 mm of rain"}[stat]
                metas.append(dict(
                    id=vid, family="stats", name=name, category=cat, order=order, unit=u, short=f"{desc[0].upper() + desc[1:]} during {wname}",
                    dataset="CERES" if vkey == "solar" else "MERRA-2", source=f"NASA POWER daily {POWER_COL.get(vkey, vname)}",
                    resolution="~100 km (CERES 1° grid)" if vkey == "solar" else "~50 km (one MERRA-2 grid cell)",
                    stage=wname, condition=cond, aggregation=agg, higher_is="neutral", station_var=station if stat == "mean" else None,
                    keywords=[vname, wname.split("(")[0], MONTH_STAGE.get(int(wkey[1:]), "") if wkey[1:].isdigit() else "", STAT_LABEL[stat]],
                    sections=dict(
                        definition=f"{desc[0].upper() + desc[1:]} during {WINDOWS[wkey][0]}. {WINDOWS[wkey][2]}",
                        why=f"{meaning} Splitting it by growth stage shows which part of the season the change is concentrated in.",
                        guide="- A positive slope means the value is rising. Compare with other months and seasons of the same variable to find when the change happens.",
                        caveats=f"- {caveat}\n- A systematically generated statistic, so its link to grower decisions is less direct than the core indicators.",
                        references="- Computed from the team data workbook, D_ daily sheets (scripts/generate_families.py)\n- NASA POWER — https://power.larc.nasa.gov/",
                    ),
                ))
                for rid, d in D.items():
                    for y in range(FIRST, LAST_YEAR + 1):
                        a = d.slice(vkey, *window_dates(wkey, y, south_by_region[rid]))
                        if a is not None and len(a):
                            v = _stat(a, stat)
                            put(rid, vid, y, v if stat == "wet" else _r(v, 3 if unit in ("0–1", "kPa") else 2))

    # ---- 2) 평년 대비 극값 일수
    EXT = {
        "tx90": ("tmax", 90, ">", "warmer-than-normal days", "heat", "worse", "days with a maximum temperature above the normal (same period, 2001–2010) top 10%"),
        "tx10": ("tmax", 10, "<", "cooler-than-normal days", "heat", "neutral", "days with a maximum temperature below the normal bottom 10%"),
        "tn90": ("tmin", 90, ">", "warmer-than-normal nights", "temp_frost", "worse", "days with a minimum temperature above the normal top 10%"),
        "tn10": ("tmin", 10, "<", "colder-than-normal nights", "temp_frost", "worse", "days with a minimum temperature below the normal bottom 10%"),
        "pr95": ("prec", 95, ">", "heavier-than-normal rain days", "rain_water", "worse", "days with more rain than the top 5% of normal rainy days (≥ 1 mm)"),
    }
    for wkey, (wname, _, wmean) in WINDOWS.items():
        for code, (vkey, pct, op, label, cat, higher, desc) in EXT.items():
            vid = f"x_{wkey}_{code}"
            order += 1
            metas.append(dict(
                id=vid, family="extremes", name=f"{wname} {label}", category=cat, order=order, unit="days",
                short=f"Number of {desc} during {wname}", dataset="MERRA-2", source=f"NASA POWER daily {POWER_COL[vkey]}",
                resolution="~50 km (one MERRA-2 grid cell)", stage=wname, condition=f"{'above' if op == '>' else 'below'} the normal (2001–2010) {pct}th percentile",
                aggregation="count", higher_is=higher, station_var=None,
                keywords=[label, wname.split("(")[0].strip(), "extremes", "normal", "unusual weather"],
                sections=dict(
                    definition=f"The number of {desc} during {wname}. {wmean} The baseline is the region's own 2001–2010 values for the same period, so each region is compared with its own normal.",
                    why="Even a small shift in the average can sharply change how often extreme days occur. This compares how much more often 'unusual days' happen in each region on the same scale.",
                    guide="- By definition, 2001–2010 averages about 10% of the days in the period (5% of rainy days for heavy rain). A rise after that means such days are becoming more frequent.",
                    caveats="- The baseline period (2001–2010) may itself already be warmer than older norms.\n- A systematically generated indicator.",
                    references="- ETCCDI percentile-index method applied per period (scripts/generate_families.py)\n- NASA POWER — https://power.larc.nasa.gov/",
                ),
            ))
            for rid, d in D.items():
                south = south_by_region[rid]
                base = [d.slice(vkey, *window_dates(wkey, y, south)) for y in BASE_YEARS]
                base = np.concatenate([b for b in base if b is not None]) if any(b is not None for b in base) else None
                if base is None:
                    continue
                if code == "pr95":
                    wet = base[base >= 1]
                    if len(wet) < 10:
                        continue
                    thr = np.percentile(wet, pct)
                else:
                    thr = np.percentile(base, pct)
                for y in range(FIRST, LAST_YEAR + 1):
                    a = d.slice(vkey, *window_dates(wkey, y, south))
                    if a is not None:
                        put(rid, vid, y, int((a > thr).sum() if op == ">" else (a < thr).sum()))

    # ---- 3) ETCCDI 27개 (시즌 1년 기준)
    def yr(d, key, y, south):
        return d.slice(key, *window_dates("year", y, south))

    etc = []

    def add(code, name, unit, cat, higher, desc, fn):
        etc.append((code, name, unit, cat, higher, desc, fn))

    add("FD", "Frost days", "days", "temp_frost", "worse", "Days with minimum temperature < 0°C", lambda d, y, s, b: (lambda a: None if a is None else int((a < 0).sum()))(yr(d, "tmin", y, s)))
    add("SU", "Summer days", "days", "heat", "worse", "Days with maximum temperature > 25°C", lambda d, y, s, b: (lambda a: None if a is None else int((a > 25).sum()))(yr(d, "tmax", y, s)))
    add("ID", "Ice days", "days", "temp_frost", "worse", "Days with maximum temperature < 0°C", lambda d, y, s, b: (lambda a: None if a is None else int((a < 0).sum()))(yr(d, "tmax", y, s)))
    add("TR", "Tropical nights", "days", "heat", "worse", "Days with minimum temperature > 20°C", lambda d, y, s, b: (lambda a: None if a is None else int((a > 20).sum()))(yr(d, "tmin", y, s)))
    add("TXx", "Hottest day of the year", "°C", "heat", "worse", "Annual maximum of daily maximum temperature", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a.max())))(yr(d, "tmax", y, s)))
    add("TNx", "Warmest night of the year", "°C", "heat", "worse", "Annual maximum of daily minimum temperature", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a.max())))(yr(d, "tmin", y, s)))
    add("TXn", "Coldest day of the year", "°C", "temp_frost", "neutral", "Annual minimum of daily maximum temperature", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a.min())))(yr(d, "tmax", y, s)))
    add("TNn", "Coldest night of the year", "°C", "temp_frost", "better", "Annual minimum of daily minimum temperature", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a.min())))(yr(d, "tmin", y, s)))
    add("TN10p", "Share of cold nights", "%", "temp_frost", "worse", "Share of days with minimum temperature below the normal bottom 10%", lambda d, y, s, b: (lambda a: None if a is None else _r(100 * float((a < b["tn10"]).mean())))(yr(d, "tmin", y, s)))
    add("TX10p", "Share of cool days", "%", "heat", "neutral", "Share of days with maximum temperature below the normal bottom 10%", lambda d, y, s, b: (lambda a: None if a is None else _r(100 * float((a < b["tx10"]).mean())))(yr(d, "tmax", y, s)))
    add("TN90p", "Share of warm nights", "%", "heat", "worse", "Share of days with minimum temperature above the normal top 10%", lambda d, y, s, b: (lambda a: None if a is None else _r(100 * float((a > b["tn90"]).mean())))(yr(d, "tmin", y, s)))
    add("TX90p", "Share of warm days", "%", "heat", "worse", "Share of days with maximum temperature above the normal top 10%", lambda d, y, s, b: (lambda a: None if a is None else _r(100 * float((a > b["tx90"]).mean())))(yr(d, "tmax", y, s)))
    add("WSDI", "Warm spell duration", "days", "heat", "worse", "Days in runs of 6+ consecutive days with maximum temperature above the normal top 10%", lambda d, y, s, b: (lambda a: None if a is None else _spell_days(a > b["tx90"]))(yr(d, "tmax", y, s)))
    add("CSDI", "Cold spell duration", "days", "temp_frost", "worse", "Days in runs of 6+ consecutive days with minimum temperature below the normal bottom 10%", lambda d, y, s, b: (lambda a: None if a is None else _spell_days(a < b["tn10"]))(yr(d, "tmin", y, s)))
    add("DTR", "Mean diurnal temperature range", "°C", "growth", "better", "Annual mean of daily (maximum − minimum) temperature", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a.mean())))(yr(d, "dtr", y, s)))
    add("Rx1day", "Wettest day of the year", "mm", "rain_water", "worse", "Annual maximum 1-day precipitation", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a.max()), 1))(yr(d, "prec", y, s)))
    add("Rx5day", "Wettest 5 days of the year", "mm", "rain_water", "worse", "Annual maximum consecutive 5-day precipitation", lambda d, y, s, b: (lambda a: None if a is None or len(a) < 5 else _r(float(np.convolve(a, np.ones(5), "valid").max()), 1))(yr(d, "prec", y, s)))
    add("SDII", "Rain intensity", "mm/day", "rain_water", "worse", "Mean precipitation on rainy days (≥ 1 mm)", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a[a >= 1].mean()) if (a >= 1).any() else 0.0))(yr(d, "prec", y, s)))
    add("R10mm", "Days with ≥ 10 mm rain", "days", "rain_water", "worse", "Days with daily precipitation ≥ 10 mm", lambda d, y, s, b: (lambda a: None if a is None else int((a >= 10).sum()))(yr(d, "prec", y, s)))
    add("R20mm", "Days with ≥ 20 mm rain", "days", "rain_water", "worse", "Days with daily precipitation ≥ 20 mm", lambda d, y, s, b: (lambda a: None if a is None else int((a >= 20).sum()))(yr(d, "prec", y, s)))
    add("R50mm", "Days with ≥ 50 mm rain", "days", "rain_water", "worse", "Days with daily precipitation ≥ 50 mm (user-defined Rnnmm)", lambda d, y, s, b: (lambda a: None if a is None else int((a >= 50).sum()))(yr(d, "prec", y, s)))
    add("CDD", "Longest dry spell", "days", "drought", "worse", "Longest run of days with precipitation < 1 mm", lambda d, y, s, b: (lambda a: None if a is None else _longest(a < 1))(yr(d, "prec", y, s)))
    add("CWD", "Longest wet spell", "days", "rain_water", "worse", "Longest run of days with precipitation ≥ 1 mm", lambda d, y, s, b: (lambda a: None if a is None else _longest(a >= 1))(yr(d, "prec", y, s)))
    add("R95p", "Very wet day rainfall", "mm", "rain_water", "worse", "Total precipitation on days above the normal top 5% of rainy days", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a[a > b["pr95"]].sum()), 1))(yr(d, "prec", y, s)))
    add("R99p", "Extremely wet day rainfall", "mm", "rain_water", "worse", "Total precipitation on days above the normal top 1% of rainy days", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a[a > b["pr99"]].sum()), 1))(yr(d, "prec", y, s)))
    add("PRCPTOT", "Total wet-day rainfall", "mm", "rain_water", "neutral", "Total precipitation on rainy days (≥ 1 mm)", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a[a >= 1].sum()), 1))(yr(d, "prec", y, s)))

    def gsl(d, y, s, b):
        start_from = date(y - 1, 7, 1) if s else date(y, 1, 1)
        end_from = date(y, 1, 1) if s else date(y, 7, 1)
        end_to = date(y, 6, 30) if s else date(y, 12, 31)
        t = d.arr["t2m"]

        def run(start, stop, cond):
            i0, i1 = (start - d.d0).days, min((stop - d.d0).days + 1, d.n)
            cur = 0
            for i in range(max(i0, 0), i1):
                if np.isnan(t[i]):
                    cur = 0
                    continue
                cur = cur + 1 if cond(t[i]) else 0
                if cur == 6:
                    return d.d0 + timedelta(days=i - 5)
            return None

        a = run(start_from, end_from - timedelta(days=1), lambda v: v > 5)
        if a is None:
            return None
        e = run(end_from, end_to, lambda v: v < 5)
        if e is None:
            if (end_to - d.d0).days >= d.n:
                return None  # 아직 끝나지 않은 해
            e = end_to
        return (e - a).days

    add("GSL", "Growing season length", "days", "growth", "neutral", "From the first 6-day run with mean temperature > 5°C to the first 6-day run < 5°C in the second half of the year", gsl)

    for code, name, unit, cat, higher, desc, fn in etc:
        vid = f"etccdi_{code.lower()}"
        order += 1
        metas.append(dict(
            id=vid, family="etccdi", name=f"{code} · {name}", category=cat, order=order, unit=unit,
            short=f"ETCCDI standard index: {desc}", dataset="MERRA-2", source="NASA POWER daily (MERRA-2)", resolution="~50 km (one MERRA-2 grid cell)",
            stage="Season year (Oct–Sep; Southern Hemisphere Apr–Mar)", condition=desc, aggregation="count" if unit == "days" else "mean",
            higher_is=higher, station_var=None, keywords=[code, name, "ETCCDI", "extremes", "WMO", "climate index"],
            sections=dict(
                definition=f"{code} is a standard index defined by the WMO Expert Team on Climate Change Detection and Indices (ETCCDI): {desc[0].lower() + desc[1:]}, computed per season year (Oct–Sep; Southern Hemisphere Apr–Mar).",
                why="Climate research worldwide uses these same definitions, so your region's change can be compared directly with results for other regions in papers and reports. It also lets you say in a presentation that standard indices reach the same conclusion.",
                guide="- Slope direction and units follow the index definition. Percentile indices use 2001–2010 as the baseline.",
                caveats="- The official ETCCDI uses calendar years, a 1961–1990 baseline and 5-day calendar windows for percentiles; here it is simplified to season years, a 2001–2010 baseline and whole-period percentiles.\n- ~50 km grid values.",
                references="- Zhang, X. et al. (2011), Indices for monitoring changes in extremes based on daily temperature and precipitation data — https://doi.org/10.1002/wcc.147\n- NASA POWER — https://power.larc.nasa.gov/",
            ),
        ))
    for rid, d in D.items():
        south = south_by_region[rid]
        base = {}
        bt = [yr(d, "tmax", y, south) for y in BASE_YEARS]
        bn = [yr(d, "tmin", y, south) for y in BASE_YEARS]
        bp = [yr(d, "prec", y, south) for y in BASE_YEARS]
        tx = np.concatenate([a for a in bt if a is not None])
        tn = np.concatenate([a for a in bn if a is not None])
        pr = np.concatenate([a for a in bp if a is not None])
        wet = pr[pr >= 1]
        base.update(tx90=np.percentile(tx, 90), tx10=np.percentile(tx, 10), tn90=np.percentile(tn, 90), tn10=np.percentile(tn, 10),
                    pr95=np.percentile(wet, 95), pr99=np.percentile(wet, 99))
        for code, *_rest, fn in etc:
            vid = f"etccdi_{code.lower()}"
            for y in range(FIRST, LAST_YEAR + 1):
                put(rid, vid, y, fn(d, y, south, base))

    return metas, values
