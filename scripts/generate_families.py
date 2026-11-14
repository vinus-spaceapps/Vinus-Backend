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
    "t2m": ("평균기온", "°C", "temp_frost", ("mean", "min", "max"), "포도의 생장·숙성 속도를 정하는 기본 기온입니다.", "50km 격자 평균이라 고도·경사면 차이는 반영되지 않습니다.", "tmean"),
    "tmin": ("최저기온", "°C", "temp_frost", ("mean", "min", "max"), "밤 기온입니다. 서리·냉해와 산도·색 유지에 영향을 줍니다.", "골짜기 바닥의 냉기는 50km 격자에서 잘 잡히지 않습니다.", "tmin"),
    "tmax": ("최고기온", "°C", "heat", ("mean", "min", "max"), "낮 기온입니다. 광합성, 일소(햇볕 데임), 산도 손실에 영향을 줍니다.", "50km 격자 평균이라 경사면 방향 차이는 반영되지 않습니다.", "tmax"),
    "dtr": ("일교차", "°C", "growth", ("mean", "min", "max"), "낮과 밤의 기온 차입니다. 클수록 색·향·산도가 잘 지켜집니다.", "격자 평균이라 골짜기·산비탈의 실제 일교차보다 작게 나옵니다.", "tmean"),
    "prec": ("강수량", "mm", "rain_water", ("sum", "max", "wet"), "물 공급원이자 병해·열과(포도알 터짐) 위험의 원인입니다.", "MERRA-2 강수는 모델에 관측을 보정한 값이라 국지성 비를 작게 잡을 수 있습니다.", None),
    "rh": ("상대습도", "%", "disease", ("mean", "min", "max"), "곰팡이병 위험과 잎의 물 손실(증산)에 영향을 줍니다.", "하루 평균값이라 밤 이슬이나 한낮 건조는 반영되지 않습니다.", None),
    "qv": ("비습", "g/kg", "disease", ("mean", "min", "max"), "공기 1kg에 든 수증기 양입니다. 덥고 눅눅한 정도를 보여 줍니다.", "하루 평균값입니다.", None),
    "vpd": ("증기압 부족(VPD)", "kPa", "drought", ("mean", "min", "max"), "공기가 잎에서 물을 빼앗는 힘입니다. 클수록 물 스트레스가 큽니다.", "일평균 기온·습도로 계산해 한낮 값보다 작게 나옵니다.", None),
    "et0": ("기준 증발산량", "mm", "drought", ("sum", "max"), "땅과 잎에서 증발로 잃는 물의 양입니다. 관수 수요를 보여 줍니다.", "기온과 위도만 쓰는 Hargreaves 식이라 바람·습도 효과는 빠져 있습니다.", None),
    "gwtop": ("겉흙 수분", "0~1", "drought", ("mean", "min", "max"), "겉흙이 얼마나 젖어 있는지(0=마름, 1=흠뻑)입니다. 짧은 가뭄을 먼저 보여 줍니다.", "모델 값이며 관수한 밭의 실제 값과 다릅니다.", None),
    "gwroot": ("뿌리층 수분", "0~1", "drought", ("mean", "min", "max"), "뿌리가 쓰는 깊은 흙의 젖음 정도입니다. 가뭄 스트레스를 보여 줍니다.", "모델 값이며 관수한 밭의 실제 값과 다릅니다.", None),
    "solar": ("일사량", "MJ/m²·일", "sun_wind", ("mean", "min", "max"), "광합성 에너지이자 당·색을 만드는 햇빛입니다. 너무 강하면 일소가 생깁니다.", "CERES 위성 1° 격자 값이며 최근 며칠은 아직 비어 있습니다.", None),
    "wind": ("풍속", "m/s", "sun_wind", ("mean", "min", "max"), "통풍으로 병을 줄이지만, 세면 가지가 꺾이고 물을 잃습니다. 약하면 복사 서리가 잘 앉습니다.", "지상 2m 하루 평균 풍속이라 순간 돌풍은 반영되지 않습니다.", None),
}
POWER_COL = {"t2m": "T2M", "tmin": "T2M_MIN", "tmax": "T2M_MAX", "prec": "PRECTOTCORR", "rh": "RH2M", "qv": "QV2M",
             "gwtop": "GWETTOP", "gwroot": "GWETROOT", "solar": "ALLSKY_SFC_SW_DWN", "wind": "WS2M"}
STAT_LABEL = {"mean": "평균", "min": "최솟값", "max": "최댓값", "sum": "합계", "wet": "비 온 날수"}

# ---------------------------------------------------------------------------
# 기간 (북반구 달 기준, 남반구는 6개월 밀어 맞춤)
# ---------------------------------------------------------------------------
MONTH_STAGE = {1: "한겨울 휴면기", 2: "휴면 끝", 3: "싹트기 전", 4: "발아기", 5: "새순 생장기", 6: "개화기", 7: "착과·알 비대기",
               8: "착색기", 9: "숙성·수확기", 10: "수확 마무리", 11: "낙엽·휴면 진입", 12: "휴면기"}
# key: (이름, [(북반구 달, 연도 오프셋)], 의미)
WINDOWS = {f"m{m:02d}": (f"{m}월({MONTH_STAGE[m]})", [(m, 0)], f"북반구 {m}월, 남반구 {(m + 5) % 12 + 1}월로, 포도의 {MONTH_STAGE[m]}에 해당합니다.") for m in range(1, 13)}
WINDOWS.update({
    "winter": ("겨울(12~2월)", [(12, -1), (1, 0), (2, 0)], "포도나무가 쉬는 한겨울입니다(남반구 6~8월)."),
    "spring": ("봄(3~5월)", [(3, 0), (4, 0), (5, 0)], "싹이 트고 새순이 자라는 시기입니다(남반구 9~11월)."),
    "summer": ("여름(6~8월)", [(6, 0), (7, 0), (8, 0)], "꽃이 피고 알이 커지며 색이 드는 시기입니다(남반구 12~2월)."),
    "autumn": ("가을(9~11월)", [(9, 0), (10, 0), (11, 0)], "포도가 익어 수확하고 가지가 여무는 시기입니다(남반구 3~5월)."),
    "gs": ("생육기(4~10월)", [(m, 0) for m in range(4, 11)], "싹이 트고 수확할 때까지의 생육기 전체입니다(남반구 10~4월)."),
    "harvest": ("수확기(8~9월)", [(8, 0), (9, 0)], "포도가 익는 마지막 두 달입니다(남반구 2~3월)."),
    "dormancy": ("휴면기(11~3월)", [(11, -1), (12, -1), (1, 0), (2, 0), (3, 0)], "잎이 진 뒤 다시 싹트기 전까지의 휴면기입니다(남반구 5~9월)."),
    "year": ("시즌 1년(10~9월)", [(m, -1) for m in (10, 11, 12)] + [(m, 0) for m in range(1, 10)], "수확 다음 달부터 그해 수확까지의 시즌 1년입니다(남반구 4~3월)."),
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
                    name, u, agg, cond = f"{wname} 비 온 날수", "일", "count", "일 강수량 ≥ 1mm"
                elif stat == "sum":
                    name, u, agg, cond = f"{wname} {vname} 합계", unit, "sum", "(조건 없음) 기간 합계"
                elif stat == "mean":
                    name, u, agg, cond = f"{wname} 평균 {vname}", unit, "mean", "(조건 없음) 기간 평균"
                else:
                    name, u, agg, cond = f"{wname} {vname} {STAT_LABEL[stat]}", unit, stat, f"(조건 없음) 기간 중 하루 {vname}의 {STAT_LABEL[stat]}"
                desc = {"mean": f"하루 {vname}을(를) 평균한 값", "min": f"하루 {vname} 가운데 가장 낮은 값", "max": f"하루 {vname} 가운데 가장 높은 값",
                        "sum": f"하루 {vname}을(를) 모두 더한 값", "wet": "하루 강수량이 1mm 이상이었던 날의 수"}[stat]
                metas.append(dict(
                    id=vid, family="stats", name=name, category=cat, order=order, unit=u, short=f"{wname} 동안 {desc}",
                    dataset="CERES" if vkey == "solar" else "MERRA-2", source=f"NASA POWER 일별 {POWER_COL.get(vkey, vname)}",
                    resolution="약 100km (CERES 1° 격자)" if vkey == "solar" else "약 50km (MERRA-2 격자 한 칸)",
                    stage=wname, condition=cond, aggregation=agg, higher_is="neutral", station_var=station if stat == "mean" else None,
                    keywords=[vname, wname.split("(")[0], MONTH_STAGE.get(int(wkey[1:]), "") if wkey[1:].isdigit() else "", STAT_LABEL[stat]],
                    sections=dict(
                        definition=f"{WINDOWS[wkey][2]} 이 기간 동안 {desc}입니다.",
                        why=f"{meaning} 생육 단계별로 쪼개 보면 변화가 어느 시기에 몰려 있는지 알 수 있습니다.",
                        guide="- 기울기가 양수면 값이 커지는 쪽입니다. 같은 변수의 다른 달·계절과 함께 보면 변화 시기를 찾을 수 있습니다.",
                        caveats=f"- {caveat}\n- 체계적으로 만든 기본 통계 지표라 생산자 결정과의 연결은 핵심 지표보다 간접적입니다.",
                        references="- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산 (scripts/generate_families.py)\n- NASA POWER — https://power.larc.nasa.gov/",
                    ),
                ))
                for rid, d in D.items():
                    for y in range(FIRST, LAST_YEAR + 1):
                        a = d.slice(vkey, *window_dates(wkey, y, south_by_region[rid]))
                        if a is not None and len(a):
                            v = _stat(a, stat)
                            put(rid, vid, y, v if stat == "wet" else _r(v, 3 if unit in ("0~1", "kPa") else 2))

    # ---- 2) 평년 대비 극값 일수
    EXT = {
        "tx90": ("tmax", 90, ">", "평년보다 더운 낮", "heat", "worse", "하루 최고기온이 평년(2001~2010년 같은 기간) 상위 10%보다 높았던 날"),
        "tx10": ("tmax", 10, "<", "평년보다 서늘한 낮", "heat", "neutral", "하루 최고기온이 평년 하위 10%보다 낮았던 날"),
        "tn90": ("tmin", 90, ">", "평년보다 따뜻한 밤", "temp_frost", "worse", "하루 최저기온이 평년 상위 10%보다 높았던 날"),
        "tn10": ("tmin", 10, "<", "평년보다 추운 밤", "temp_frost", "worse", "하루 최저기온이 평년 하위 10%보다 낮았던 날"),
        "pr95": ("prec", 95, ">", "평년 기준 큰비 날", "rain_water", "worse", "하루 강수량이 평년 비 온 날(1mm 이상)의 상위 5%보다 많았던 날"),
    }
    for wkey, (wname, _, wmean) in WINDOWS.items():
        for code, (vkey, pct, op, label, cat, higher, desc) in EXT.items():
            vid = f"x_{wkey}_{code}"
            order += 1
            metas.append(dict(
                id=vid, family="extremes", name=f"{wname} {label} 일수", category=cat, order=order, unit="일",
                short=f"{wname} 동안 {desc}의 수", dataset="MERRA-2", source=f"NASA POWER 일별 {POWER_COL[vkey]}",
                resolution="약 50km (MERRA-2 격자 한 칸)", stage=wname, condition=f"평년(2001~2010) {pct} 백분위 {'초과' if op == '>' else '미만'}",
                aggregation="count", higher_is=higher, station_var=None,
                keywords=[label, wname.split("(")[0], "극값", "평년", "이상 기후"],
                sections=dict(
                    definition=f"{wmean} 이 기간 동안 {desc}의 수입니다. 기준은 그 산지의 2001~2010년 같은 기간 값이라, 산지마다 자기 평소와 비교합니다.",
                    why="평균이 조금 바뀌어도 극단적인 날은 크게 늘거나 줄 수 있습니다. 산지마다 '평소와 다른 날'이 얼마나 잦아졌는지 같은 잣대로 비교할 수 있습니다.",
                    guide="- 2001~2010년은 정의상 기간 날 수의 약 10%(큰비는 비 온 날의 5%)입니다. 이후 늘면 그런 날이 잦아진 것입니다.",
                    caveats="- 기준 기간(2001~2010) 자체가 이미 따뜻해진 시기일 수 있습니다.\n- 체계적으로 만든 지표입니다.",
                    references="- ETCCDI 백분위 지수 방식을 기간별로 적용 (scripts/generate_families.py)\n- NASA POWER — https://power.larc.nasa.gov/",
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

    add("FD", "서리일수", "일", "temp_frost", "worse", "하루 최저기온 < 0°C 인 날 수", lambda d, y, s, b: (lambda a: None if a is None else int((a < 0).sum()))(yr(d, "tmin", y, s)))
    add("SU", "여름일수", "일", "heat", "worse", "하루 최고기온 > 25°C 인 날 수", lambda d, y, s, b: (lambda a: None if a is None else int((a > 25).sum()))(yr(d, "tmax", y, s)))
    add("ID", "결빙일수", "일", "temp_frost", "worse", "하루 최고기온 < 0°C 인 날 수", lambda d, y, s, b: (lambda a: None if a is None else int((a < 0).sum()))(yr(d, "tmax", y, s)))
    add("TR", "열대야일수", "일", "heat", "worse", "하루 최저기온 > 20°C 인 날 수", lambda d, y, s, b: (lambda a: None if a is None else int((a > 20).sum()))(yr(d, "tmin", y, s)))
    add("TXx", "연 최고 낮기온", "°C", "heat", "worse", "하루 최고기온의 연 최댓값", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a.max())))(yr(d, "tmax", y, s)))
    add("TNx", "연 최고 밤기온", "°C", "heat", "worse", "하루 최저기온의 연 최댓값", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a.max())))(yr(d, "tmin", y, s)))
    add("TXn", "연 최저 낮기온", "°C", "temp_frost", "neutral", "하루 최고기온의 연 최솟값", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a.min())))(yr(d, "tmax", y, s)))
    add("TNn", "연 최저 밤기온", "°C", "temp_frost", "better", "하루 최저기온의 연 최솟값", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a.min())))(yr(d, "tmin", y, s)))
    add("TN10p", "추운 밤 비율", "%", "temp_frost", "worse", "하루 최저기온이 평년 하위 10%보다 낮은 날의 비율", lambda d, y, s, b: (lambda a: None if a is None else _r(100 * float((a < b["tn10"]).mean())))(yr(d, "tmin", y, s)))
    add("TX10p", "서늘한 낮 비율", "%", "heat", "neutral", "하루 최고기온이 평년 하위 10%보다 낮은 날의 비율", lambda d, y, s, b: (lambda a: None if a is None else _r(100 * float((a < b["tx10"]).mean())))(yr(d, "tmax", y, s)))
    add("TN90p", "따뜻한 밤 비율", "%", "heat", "worse", "하루 최저기온이 평년 상위 10%보다 높은 날의 비율", lambda d, y, s, b: (lambda a: None if a is None else _r(100 * float((a > b["tn90"]).mean())))(yr(d, "tmin", y, s)))
    add("TX90p", "더운 낮 비율", "%", "heat", "worse", "하루 최고기온이 평년 상위 10%보다 높은 날의 비율", lambda d, y, s, b: (lambda a: None if a is None else _r(100 * float((a > b["tx90"]).mean())))(yr(d, "tmax", y, s)))
    add("WSDI", "더위 지속 일수", "일", "heat", "worse", "최고기온이 평년 상위 10%를 넘는 날이 6일 이상 이어진 구간에 속한 날 수", lambda d, y, s, b: (lambda a: None if a is None else _spell_days(a > b["tx90"]))(yr(d, "tmax", y, s)))
    add("CSDI", "추위 지속 일수", "일", "temp_frost", "worse", "최저기온이 평년 하위 10%보다 낮은 날이 6일 이상 이어진 구간에 속한 날 수", lambda d, y, s, b: (lambda a: None if a is None else _spell_days(a < b["tn10"]))(yr(d, "tmin", y, s)))
    add("DTR", "연평균 일교차", "°C", "growth", "better", "하루 (최고기온 − 최저기온)의 연평균", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a.mean())))(yr(d, "dtr", y, s)))
    add("Rx1day", "연 최대 1일 강수량", "mm", "rain_water", "worse", "하루 강수량의 연 최댓값", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a.max()), 1))(yr(d, "prec", y, s)))
    add("Rx5day", "연 최대 5일 강수량", "mm", "rain_water", "worse", "연속 5일 강수량 합의 연 최댓값", lambda d, y, s, b: (lambda a: None if a is None or len(a) < 5 else _r(float(np.convolve(a, np.ones(5), "valid").max()), 1))(yr(d, "prec", y, s)))
    add("SDII", "강수 강도", "mm/일", "rain_water", "worse", "비 온 날(≥1mm)의 하루 평균 강수량", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a[a >= 1].mean()) if (a >= 1).any() else 0.0))(yr(d, "prec", y, s)))
    add("R10mm", "10mm 이상 강수일", "일", "rain_water", "worse", "하루 강수량 ≥ 10mm 인 날 수", lambda d, y, s, b: (lambda a: None if a is None else int((a >= 10).sum()))(yr(d, "prec", y, s)))
    add("R20mm", "20mm 이상 강수일", "일", "rain_water", "worse", "하루 강수량 ≥ 20mm 인 날 수", lambda d, y, s, b: (lambda a: None if a is None else int((a >= 20).sum()))(yr(d, "prec", y, s)))
    add("R50mm", "50mm 이상 강수일", "일", "rain_water", "worse", "하루 강수량 ≥ 50mm 인 날 수 (사용자 정의 Rnnmm)", lambda d, y, s, b: (lambda a: None if a is None else int((a >= 50).sum()))(yr(d, "prec", y, s)))
    add("CDD", "최장 무강수 기간", "일", "drought", "worse", "하루 강수량 < 1mm 인 날이 가장 길게 이어진 일수", lambda d, y, s, b: (lambda a: None if a is None else _longest(a < 1))(yr(d, "prec", y, s)))
    add("CWD", "최장 연속 강수 기간", "일", "rain_water", "worse", "하루 강수량 ≥ 1mm 인 날이 가장 길게 이어진 일수", lambda d, y, s, b: (lambda a: None if a is None else _longest(a >= 1))(yr(d, "prec", y, s)))
    add("R95p", "매우 많은 비의 양", "mm", "rain_water", "worse", "평년 비 온 날의 상위 5%를 넘는 날 강수량의 합", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a[a > b["pr95"]].sum()), 1))(yr(d, "prec", y, s)))
    add("R99p", "극히 많은 비의 양", "mm", "rain_water", "worse", "평년 비 온 날의 상위 1%를 넘는 날 강수량의 합", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a[a > b["pr99"]].sum()), 1))(yr(d, "prec", y, s)))
    add("PRCPTOT", "비 온 날 강수 총량", "mm", "rain_water", "neutral", "비 온 날(≥1mm) 강수량의 합", lambda d, y, s, b: (lambda a: None if a is None else _r(float(a[a >= 1].sum()), 1))(yr(d, "prec", y, s)))

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

    add("GSL", "생육 가능 기간", "일", "growth", "neutral", "평균기온 > 5°C 가 6일 이어진 첫날부터 하반기에 < 5°C 가 6일 이어진 첫날까지", gsl)

    for code, name, unit, cat, higher, desc, fn in etc:
        vid = f"etccdi_{code.lower()}"
        order += 1
        metas.append(dict(
            id=vid, family="etccdi", name=f"{code} · {name}", category=cat, order=order, unit=unit,
            short=f"ETCCDI 표준 지수: {desc}", dataset="MERRA-2", source="NASA POWER 일별 (MERRA-2)", resolution="약 50km (MERRA-2 격자 한 칸)",
            stage="시즌 1년 (전년 10월~9월, 남반구 전년 4월~3월)", condition=desc, aggregation="count" if unit == "일" else "mean",
            higher_is=higher, station_var=None, keywords=[code, name, "ETCCDI", "극값", "WMO", "기후 지수"],
            sections=dict(
                definition=f"세계기상기구(WMO) 기후변화 탐지·지수 전문가팀(ETCCDI)이 정한 표준 지수 {code}입니다. {desc}을(를) 시즌 1년(전년 10월~9월, 남반구 전년 4월~3월) 단위로 계산했습니다.",
                why="전 세계 기후 연구가 같은 정의로 쓰는 지수라, 우리 산지의 변화를 논문·보고서의 다른 지역 결과와 바로 비교할 수 있습니다. 발표에서 '표준 지표로도 같은 결론'이라는 근거가 됩니다.",
                guide="- 기울기 방향과 단위는 지수 정의를 따릅니다. 백분위 지수의 기준 기간은 2001~2010년입니다.",
                caveats="- 원래 ETCCDI는 달력 1년·1961~1990년 기준이고 백분위는 날짜별 5일 창으로 정하지만, 여기서는 시즌 1년·2001~2010년·기간 전체 백분위로 단순화했습니다.\n- 50km 격자 값입니다.",
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
