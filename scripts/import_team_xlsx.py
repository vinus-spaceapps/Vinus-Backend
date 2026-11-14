"""팀 데이터 엑셀(NASA_와인_데이터정리.xlsx) → data/series CSV + 검증 자료.

사용:
    .venv/bin/pip install openpyxl
    .venv/bin/python scripts/import_team_xlsx.py ~/Downloads/NASA_와인_데이터정리.xlsx

읽는 시트
- 7_연도별지표        → data/series/<변수>/<산지>.csv (기준값이 다른 열은 <산지>__t<기준값>.csv)
- 15_전전A_MODIS연도별 → spring_night_lst
- 8_MODIS그린업       → greenup_doy
- D_<산지> (일별 원자료, NASA POWER) → 새 지표 13개 + 팀 지표의 추가 기준값 (DERIVED 표)
- 11_전전C_관측소오차, 14_전전A_MODIS요약 → data/validation.json
- 6_추세검정결과       → tests/fixtures/team_trend_results.csv (엔진 대조 테스트용)

엑셀 파일 자체는 커밋하지 않습니다. 다시 받으면 이 스크립트만 다시 돌리면 됩니다.
"""

from __future__ import annotations

import csv
import json
import math
import sys
from datetime import date, timedelta
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
SERIES = ROOT / "data" / "series"

REGION_MAP = {
    "부르고뉴_본": "burgundy",
    "보르도_생테밀리옹": "bordeaux",
    "모젤_베른카스텔": "mosel",
    "오카나간_올리버": "okanagan",
    "나파": "napa",
    "바로사_타눈다": "barossa",
    "영동": "yeongdong",
}

# 7_연도별지표 열 이름 → (변수 id, 기준값). 기준값이 None 이면 지표 md 의 기본 기준값.
COLUMN_MAP = {
    "봄 서리일수(Tmin≤0°C)": ("frost_after_budburst", None),
    "봄 강한서리일수(Tmin≤−2°C)": ("frost_after_budburst", -2),
    "겨울 최저기온": ("winter_min_temp", None),
    "생육기 적산온도 GDD(기준10°C)": ("gdd_growing_season", None),
    "Huglin 지수": ("huglin_index", None),
    "폭염일수(Tmax≥35°C)": ("heat_days", None),
    "고온일수(Tmax≥30°C)": ("heat_days", 30),
    "서늘한 밤 지수": ("cool_night_index", None),
    "수확기 강수량": ("harvest_rain_total", None),
    "수확기 호우일수(≥20mm)": ("harvest_rain_days", None),
    "생육기 고습일수(RH≥80%, 15~25°C)": ("humid_days", None),
    "생육기 뿌리층 토양수분": ("gs_soil_moisture", None),
}


def num(x):
    if x is None or x == "" or x == -999:
        return None
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def series_path(var_id: str, region_id: str, threshold) -> Path:
    name = f"{region_id}.csv" if threshold is None else f"{region_id}__t{float(threshold):g}.csv"
    return SERIES / var_id / name


def write_series(store: dict) -> int:
    count = 0
    for (var_id, region_id, thr), points in sorted(store.items(), key=lambda kv: str(kv[0])):
        path = series_path(var_id, region_id, thr)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["year", "value"])
            for year in sorted(points):
                v = points[year]
                w.writerow([year, int(v) if float(v).is_integer() else round(v, 4)])
        count += 1
    return count


# ---------------------------------------------------------------------------
# 일별 원자료 → 연도별 지표
#  - 시즌 연도는 수확 연도 (남반구 2026 시즌 = 2025년 10월 ~ 2026년 4월)
#  - 기간의 95% 이상 자료가 있어야 그해 값을 냄
#  - 팀 지표 정의는 7_연도별지표와 일별 재계산으로 맞춰 확인했음 (check_team_definitions)
# ---------------------------------------------------------------------------

SOUTH = {"바로사_타눈다"}
COVERAGE = 0.95


def read_daily(wb, region) -> dict:
    it = wb[f"D_{region}"].iter_rows(values_only=True)
    header = next(it)
    out = {}
    for r in it:
        if not r or not r[0]:
            continue
        rec = {}
        for k, v in zip(header[1:], r[1:]):
            rec[k] = num(v)
        out[date.fromisoformat(str(r[0])[:10])] = rec
    return out


def days(start: date, end: date):
    d = start
    while d <= end:
        yield d
        d += timedelta(days=1)


def window(D, start, end, key):
    """기간 안의 (날짜, 값). 자료가 95% 미만이면 None."""
    want = list(days(start, end))
    got = [(d, D[d][key]) for d in want if d in D and D[d].get(key) is not None]
    if not want or len(got) < COVERAGE * len(want):
        return None
    return got


def gs(y, south):  # 생육기
    return (date(y - 1, 10, 1), date(y, 4, 30)) if south else (date(y, 4, 1), date(y, 10, 31))


def harvest(y, south):  # 수확기
    return (date(y, 2, 1), date(y, 3, 31)) if south else (date(y, 8, 1), date(y, 9, 30))


def spring(y, south):  # 봄 서리 시기 (팀 서리일수와 같은 창: 4~5월, 남반구 10~11월)
    return (date(y - 1, 10, 1), date(y - 1, 11, 30)) if south else (date(y, 4, 1), date(y, 5, 31))


def frost_half(y, south, which):  # 마지막 봄 서리 / 첫 가을 서리를 찾는 반년
    if which == "spring":
        return (date(y - 1, 7, 1), date(y - 1, 12, 31)) if south else (date(y, 1, 1), date(y, 6, 30))
    return (date(y, 1, 1), date(y, 6, 30)) if south else (date(y, 7, 1), date(y, 12, 31))


def agg(key, win, op, thr=None):
    def f(D, y, south):
        s, e = win(y, south)
        w = window(D, s, e, key)
        if w is None:
            return None
        vals = [v for _, v in w]
        if op == "mean":
            return round(sum(vals) / len(vals), 2)
        if op == "sum":
            return round(sum(vals), 1)
        if op == "min":
            return round(min(vals), 2)
        if op == "count_le":
            return sum(v <= thr for v in vals)
        if op == "count_ge":
            return sum(v >= thr for v in vals)
        raise ValueError(op)

    return f


def dtr(D, y, south):
    s, e = gs(y, south)
    hi, lo = window(D, s, e, "T2M_MAX"), window(D, s, e, "T2M_MIN")
    if hi is None or lo is None:
        return None
    lo_by = dict(lo)
    diffs = [v - lo_by[d] for d, v in hi if d in lo_by]
    return round(sum(diffs) / len(diffs), 2)


def bedd(D, y, south):
    """유효 적산온도(단순형): Σ min(max(평균기온−10, 0), 9). 19°C 넘는 열은 숙성에 더 보태지 않는다고 봄."""
    s, e = gs(y, south)
    w = window(D, s, e, "T2M")
    if w is None:
        return None
    return round(sum(min(max(v - 10, 0), 9) for _, v in w), 1)


def dry_spell(D, y, south):
    s, e = gs(y, south)
    w = window(D, s, e, "PRECTOTCORR")
    if w is None:
        return None
    best = cur = 0
    for _, v in w:
        cur = cur + 1 if v < 1 else 0
        best = max(best, cur)
    return best


def _season_day(d: date, south: bool) -> int:
    """연중일. 남반구는 7월 1일을 1로 셈 (봄이 해를 넘지 않게)."""
    if south:
        base = date(d.year if d.month >= 7 else d.year - 1, 7, 1)
        return (d - base).days + 1
    return d.timetuple().tm_yday


def _last_frost(D, y, south, thr):
    s, e = frost_half(y, south, "spring")
    w = window(D, s, e, "T2M_MIN")
    if w is None:
        return "na"
    hits = [d for d, v in w if v <= thr]
    return hits[-1] if hits else None


def _first_frost(D, y, south, thr):
    s, e = frost_half(y, south, "autumn")
    w = window(D, s, e, "T2M_MIN")
    if w is None:
        return "na"
    hits = [d for d, v in w if v <= thr]
    return hits[0] if hits else None


def last_spring_frost(thr):
    def f(D, y, south):
        d = _last_frost(D, y, south, thr)
        return None if d in ("na", None) else _season_day(d, south)

    return f


def frost_free(thr):
    def f(D, y, south):
        a, b = _last_frost(D, y, south, thr), _first_frost(D, y, south, thr)
        if a == "na" or b == "na" or (a is None and b is None):
            return None  # 자료 부족이거나 그해 서리가 아예 없으면 계산하지 않음
        start = a or frost_half(y, south, "spring")[0]
        end = b or frost_half(y, south, "autumn")[1]
        return (end - start).days - 1

    return f


# 산지별 계산 맥락 (위도, MODIS 그린업 날짜). main() 이 산지마다 채웁니다.
CTX: dict = {"lat": 0.0, "greenup": {}}


def flowering(y, south):  # 개화기 (6월, 남반구 12월)
    return (date(y - 1, 12, 1), date(y - 1, 12, 31)) if south else (date(y, 6, 1), date(y, 6, 30))


def spring3(y, south):  # 봄 석 달 (3~5월, 남반구 9~11월) — 싹트는 시기를 정하는 기온
    return (date(y - 1, 9, 1), date(y - 1, 11, 30)) if south else (date(y, 3, 1), date(y, 5, 31))


def early_season(y, south):  # 생육 초기 (4~6월, 남반구 10~12월) — 노균병 1차 감염 시기
    return (date(y - 1, 10, 1), date(y - 1, 12, 31)) if south else (date(y, 4, 1), date(y, 6, 30))


def dormancy(y, south):  # 휴면기 (11~3월, 남반구 5~9월) — 저온 충족·겨울 강수
    return (date(y - 1, 5, 1), date(y - 1, 9, 30)) if south else (date(y - 1, 11, 1), date(y, 3, 31))


def team_winter(y, south):  # 팀 '겨울 최저기온'과 같은 겨울 (12~2월, 남반구 같은 해 6~8월)
    if south:
        return (date(y, 6, 1), date(y, 8, 31))
    end = date(y, 3, 1) - timedelta(days=1)
    return (date(y - 1, 12, 1), end)


def multi(keys, win, rule):
    """여러 변수를 같은 날짜로 묶어 rule(rec) 이 참인 날을 셉니다."""
    def f(D, y, south):
        s, e = win(y, south)
        want = list(days(s, e))
        recs = [D[d] for d in want if d in D and all(D[d].get(k) is not None for k in keys)]
        if not want or len(recs) < COVERAGE * len(want):
            return None
        return sum(1 for r in recs if rule(r))

    return f


def longest_run(key, win, cond):
    def f(D, y, south):
        s, e = win(y, south)
        w = window(D, s, e, key)
        if w is None:
            return None
        best = cur = 0
        for _, v in w:
            cur = cur + 1 if cond(v) else 0
            best = max(best, cur)
        return best

    return f


def max_of(key, win):
    def f(D, y, south):
        s, e = win(y, south)
        w = window(D, s, e, key)
        return None if w is None else round(max(v for _, v in w), 1)

    return f


def dtr_in(win):
    def f(D, y, south):
        s, e = win(y, south)
        hi, lo = window(D, s, e, "T2M_MAX"), window(D, s, e, "T2M_MIN")
        if hi is None or lo is None:
            return None
        lo_by = dict(lo)
        diffs = [v - lo_by[d] for d, v in hi if d in lo_by]
        return round(sum(diffs) / len(diffs), 2)

    return f


def first_autumn_frost(thr):
    def f(D, y, south):
        d = _first_frost(D, y, south, thr)
        return None if d in ("na", None) else d.timetuple().tm_yday

    return f


def greenup_frost(thr, n_days=30):
    """MODIS 그린업 날짜부터 30일 동안 최저기온 ≤ 기준값인 날 수 (기획서의 원래 '싹튼 뒤 서리' 정의)."""
    def f(D, y, south):
        if south:
            return None  # 남반구 그린업은 겨울 목초를 잡아 포도 발아와 맞지 않음
        g = CTX["greenup"].get(y)
        if g is None:
            return None
        w = window(D, g, g + timedelta(days=n_days - 1), "T2M_MIN")
        return None if w is None else sum(v <= thr for _, v in w)

    return f


def _es(t):  # 포화 수증기압 (kPa)
    return 0.6108 * math.exp(17.27 * t / (t + 237.3))


def vpd_mean(D, y, south):
    s, e = gs(y, south)
    want = list(days(s, e))
    recs = [D[d] for d in want if d in D and D[d].get("T2M") is not None and D[d].get("RH2M") is not None]
    if not want or len(recs) < COVERAGE * len(want):
        return None
    return round(sum(_es(r["T2M"]) * (1 - r["RH2M"] / 100) for r in recs) / len(recs), 3)


def _ra(lat_deg, d: date) -> float:
    """대기 상단 일사량 Ra (MJ/m²/일), FAO-56 식 21."""
    j = d.timetuple().tm_yday
    phi = math.radians(lat_deg)
    dr = 1 + 0.033 * math.cos(2 * math.pi * j / 365)
    dec = 0.409 * math.sin(2 * math.pi * j / 365 - 1.39)
    ws = math.acos(max(-1.0, min(1.0, -math.tan(phi) * math.tan(dec))))
    return 24 * 60 / math.pi * 0.0820 * dr * (ws * math.sin(phi) * math.sin(dec) + math.cos(phi) * math.cos(dec) * math.sin(ws))


def water_balance(D, y, south):
    """생육기 (강수 − 기준 증발산 ET0). ET0 는 Hargreaves 식(FAO-56 식 52)."""
    s, e = gs(y, south)
    want = list(days(s, e))
    keys = ("T2M", "T2M_MAX", "T2M_MIN", "PRECTOTCORR")
    ok = [d for d in want if d in D and all(D[d].get(k) is not None for k in keys)]
    if not want or len(ok) < COVERAGE * len(want):
        return None
    total = 0.0
    for d in ok:
        r = D[d]
        et0 = 0.0023 * (r["T2M"] + 17.8) * math.sqrt(max(r["T2M_MAX"] - r["T2M_MIN"], 0)) * 0.408 * _ra(CTX["lat"], d)
        total += r["PRECTOTCORR"] - et0
    return round(total, 1)


# --- 3차: 생육 단계별로 더 잘게 나눈 지표용 기간·함수 -------------------------------


def summer(y, south):  # 여름 한 달 (7월, 남반구 1월) — 착과~착색 사이 알이 크는 시기
    return (date(y, 1, 1), date(y, 1, 31)) if south else (date(y, 7, 1), date(y, 7, 31))


def summer2(y, south):  # 여름 두 달 (7~8월, 남반구 1~2월) — 착색 전후 물 스트레스
    return (date(y, 1, 1), date(y, 2, 28)) if south else (date(y, 7, 1), date(y, 8, 31))


def autumn(y, south):  # 수확 뒤 가을 (10~11월, 남반구 4~5월) — 가지가 여물어 겨울을 준비
    return (date(y, 4, 1), date(y, 5, 31)) if south else (date(y, 10, 1), date(y, 11, 30))


def water_year(y, south):  # 시즌 1년 (전년 10월~9월, 남반구 전년 4월~3월)
    return (date(y - 1, 4, 1), date(y, 3, 31)) if south else (date(y - 1, 10, 1), date(y, 9, 30))


def spring_plus(y, south):  # 봄 + 하루 전 (전날과 비교하는 급랭 계산용)
    s, e = spring(y, south)
    return (s - timedelta(days=1), e)


def recs_in(D, win, y, south, keys):
    s, e = win(y, south)
    want = list(days(s, e))
    got = [(d, D[d]) for d in want if d in D and all(D[d].get(k) is not None for k in keys)]
    if not want or len(got) < COVERAGE * len(want):
        return None
    return got


def excess_sum(key, win, thr, below=False):
    """기준값을 넘은(below=True 면 밑돈) 만큼을 모두 더함."""
    def f(D, y, south):
        s, e = win(y, south)
        w = window(D, s, e, key)
        if w is None:
            return None
        return round(sum(max(0.0, (thr - v) if below else (v - thr)) for _, v in w), 1)

    return f


def spring_cold_snaps(D, y, south):
    """봄에 하루 평균기온이 전날보다 5°C 이상 떨어진 날 수."""
    w = recs_in(D, spring_plus, y, south, ("T2M",))
    if w is None:
        return None
    vals = [r["T2M"] for _, r in w]
    return sum(1 for a, b in zip(vals, vals[1:]) if b - a <= -5)


def rain_intensity(D, y, south):
    s, e = gs(y, south)
    w = window(D, s, e, "PRECTOTCORR")
    if w is None:
        return None
    wet = [v for _, v in w if v >= 1]
    return round(sum(wet) / len(wet), 2) if wet else 0.0


def rx5day(D, y, south):
    s, e = gs(y, south)
    w = window(D, s, e, "PRECTOTCORR")
    if w is None or len(w) < 5:
        return None
    vals = [v for _, v in w]
    return round(max(sum(vals[i:i + 5]) for i in range(len(vals) - 4)), 1)


def water_balance_in(win):
    def f(D, y, south):
        w = recs_in(D, win, y, south, ("T2M", "T2M_MAX", "T2M_MIN", "PRECTOTCORR"))
        if w is None:
            return None
        total = 0.0
        for d, r in w:
            total += r["PRECTOTCORR"] - _et0(r, d)
        return round(total, 1)

    return f


def _et0(r, d):
    return 0.0023 * (r["T2M"] + 17.8) * math.sqrt(max(r["T2M_MAX"] - r["T2M_MIN"], 0)) * 0.408 * _ra(CTX["lat"], d)


def et0_sum(D, y, south):
    w = recs_in(D, gs, y, south, ("T2M", "T2M_MAX", "T2M_MIN"))
    return None if w is None else round(sum(_et0(r, d) for d, r in w), 1)


def vpd_count(win, thr):
    def f(D, y, south):
        w = recs_in(D, win, y, south, ("T2M", "RH2M"))
        return None if w is None else sum(1 for _, r in w if _es(r["T2M"]) * (1 - r["RH2M"] / 100) >= thr)

    return f


def soil_drought_days(D, y, south):
    """뿌리층 토양수분이 그 산지 2001~2010년 생육기의 하위 20% 아래로 내려간 날 수."""
    p20 = CTX.get("soil_p20")
    if p20 is None:
        return None
    s, e = gs(y, south)
    w = window(D, s, e, "GWETROOT")
    return None if w is None else sum(1 for _, v in w if v < p20)


def sky_days(win, cond):
    """맑음·흐림: 실제 일사량 / 맑은 날 일사량(Rso = 0.75 × Ra, FAO-56) 비율로 판단."""
    def f(D, y, south):
        w = recs_in(D, win, y, south, ("ALLSKY_SFC_SW_DWN",))
        if w is None:
            return None
        return sum(1 for d, r in w if cond(r["ALLSKY_SFC_SW_DWN"] / max(0.75 * _ra(CTX["lat"], d), 0.1)))

    return f


def _dewpoint(t, rh):
    g = math.log(max(rh, 1) / 100) + 17.27 * t / (237.3 + t)
    return 237.3 * g / (17.27 - g)


def dew_days(D, y, south):
    """수확기에 밤 최저기온이 이슬점 + 1°C 이하로 내려가 이슬이 맺히기 쉬운 날 수."""
    w = recs_in(D, harvest, y, south, ("T2M", "RH2M", "T2M_MIN"))
    return None if w is None else sum(1 for _, r in w if r["T2M_MIN"] <= _dewpoint(r["T2M"], r["RH2M"]) + 1)


def _run_start(D, start: date, end: date, cond, n=5):
    run = 0
    for d in days(start, end):
        r = D.get(d)
        if r is None or r.get("T2M") is None:
            run = 0
            continue
        run = run + 1 if cond(r["T2M"]) else 0
        if run == n:
            return d - timedelta(days=n - 1)
    return None


def _gs_start_date(D, y, south):
    s = date(y - 1, 7, 1) if south else date(y, 1, 1)
    e = date(y - 1, 12, 31) if south else date(y, 7, 31)
    return _run_start(D, s, e, lambda t: t >= 10)


def _gs_end_date(D, y, south):
    s = date(y, 2, 1) if south else date(y, 8, 1)
    e = date(y, 7, 31) if south else date(y, 12, 31)
    return _run_start(D, s, e, lambda t: t < 10)


def thermal_start(D, y, south):
    d = _gs_start_date(D, y, south)
    return None if d is None else _season_day(d, south)


def thermal_end(D, y, south):
    d = _gs_end_date(D, y, south)
    return None if d is None else _season_day(d, south)


def thermal_length(D, y, south):
    a, b = _gs_start_date(D, y, south), _gs_end_date(D, y, south)
    return None if a is None or b is None else (b - a).days


def gdd_milestone(target):
    """생육기 시작(4/1, 남반구 10/1)부터 적산온도가 target 에 닿은 날."""
    def f(D, y, south):
        s, e = gs(y, south)
        total = 0.0
        for d in days(s, e):
            r = D.get(d)
            if r is None or r.get("T2M") is None:
                continue
            total += max(0.0, r["T2M"] - 10)
            if total >= target:
                return _season_day(d, south)
        return None

    return f


def early_spring_gdd(D, y, south):
    """이른 봄(1~3월, 남반구 7~9월) Σ max(0, 평균기온 − 5). 싹을 깨우는 온기."""
    win = (lambda yy, ss: (date(yy - 1, 7, 1), date(yy - 1, 9, 30)) if ss else (date(yy, 1, 1), date(yy, 3, 31)))
    return excess_sum("T2M", win, 5)(D, y, south)


# (변수 id, 기준값(None=기본), 계산 함수)
DERIVED = [
    # 3차로 더한 지표 — 기온
    ("winter_mean_temp", None, agg("T2M", team_winter, "mean")),
    ("summer_mean_temp", None, agg("T2M", summer, "mean")),
    ("autumn_mean_temp", None, agg("T2M", autumn, "mean")),
    ("gs_tmax_mean", None, agg("T2M_MAX", gs, "mean")),
    ("gs_tmin_mean", None, agg("T2M_MIN", gs, "mean")),
    ("harvest_tmax_mean", None, agg("T2M_MAX", harvest, "mean")),
    ("harvest_tmin_mean", None, agg("T2M_MIN", harvest, "mean")),
    ("hottest_day", None, max_of("T2M_MAX", gs)),
    ("harvest_warm_nights", None, agg("T2M_MIN", harvest, "count_ge", 15)),
    ("harvest_warm_nights", 12, agg("T2M_MIN", harvest, "count_ge", 12)),
    ("harvest_warm_nights", 18, agg("T2M_MIN", harvest, "count_ge", 18)),
    ("harvest_hot_days", None, agg("T2M_MAX", harvest, "count_ge", 30)),
    ("harvest_hot_days", 32, agg("T2M_MAX", harvest, "count_ge", 32)),
    ("harvest_hot_days", 35, agg("T2M_MAX", harvest, "count_ge", 35)),
    ("flowering_cold_days", None, multi(("T2M",), flowering, lambda r: r["T2M"] < 15)),
    ("flowering_hot_days", None, agg("T2M_MAX", flowering, "count_ge", 32)),
    ("flowering_hot_days", 30, agg("T2M_MAX", flowering, "count_ge", 30)),
    ("flowering_hot_days", 35, agg("T2M_MAX", flowering, "count_ge", 35)),
    ("early_spring_gdd", None, early_spring_gdd),
    ("ice_days", None, multi(("T2M_MAX",), team_winter, lambda r: r["T2M_MAX"] <= 0)),
    ("winter_warm_days", None, agg("T2M_MAX", team_winter, "count_ge", 15)),
    ("winter_warm_days", 10, agg("T2M_MAX", team_winter, "count_ge", 10)),
    ("spring_cold_snaps", None, spring_cold_snaps),
    ("heat_degree_sum", None, excess_sum("T2M_MAX", gs, 35)),
    ("heat_degree_sum", 32, excess_sum("T2M_MAX", gs, 32)),
    ("winter_cold_sum", None, excess_sum("T2M_MIN", team_winter, -10, below=True)),
    ("annual_frost_days", None, agg("T2M_MIN", water_year, "count_le", 0)),
    # 비·물
    ("spring_rain", None, agg("PRECTOTCORR", spring, "sum")),
    ("summer_rain", None, agg("PRECTOTCORR", summer, "sum")),
    ("annual_rain", None, agg("PRECTOTCORR", water_year, "sum")),
    ("harvest_wet_days", None, agg("PRECTOTCORR", harvest, "count_ge", 1)),
    ("harvest_max_rain", None, max_of("PRECTOTCORR", harvest)),
    ("rx5day_gs", None, rx5day),
    ("gs_heavy_rain_days", None, agg("PRECTOTCORR", gs, "count_ge", 30)),
    ("gs_heavy_rain_days", 20, agg("PRECTOTCORR", gs, "count_ge", 20)),
    ("gs_heavy_rain_days", 50, agg("PRECTOTCORR", gs, "count_ge", 50)),
    ("harvest_dry_spell", None, longest_run("PRECTOTCORR", harvest, lambda v: v < 1)),
    ("rain_intensity_gs", None, rain_intensity),
    ("wet_spell_max_gs", None, longest_run("PRECTOTCORR", gs, lambda v: v >= 1)),
    ("harvest_wet_spell", None, longest_run("PRECTOTCORR", harvest, lambda v: v >= 1)),
    ("spring_wet_days", None, agg("PRECTOTCORR", spring, "count_ge", 1)),
    ("flowering_wet_days", None, agg("PRECTOTCORR", flowering, "count_ge", 1)),
    ("water_balance_harvest", None, water_balance_in(harvest)),
    ("water_balance_summer", None, water_balance_in(summer2)),
    ("et0_gs", None, et0_sum),
    # 습도·병해
    ("gs_rh_mean", None, agg("RH2M", gs, "mean")),
    ("hot_humid_days", None, multi(("T2M", "RH2M"), gs, lambda r: r["T2M"] >= 25 and r["RH2M"] >= 70)),
    ("dry_air_days", None, multi(("RH2M",), gs, lambda r: r["RH2M"] < 40)),
    ("vpd_high_days", None, vpd_count(gs, 1.5)),
    ("botrytis_days", None, multi(("T2M", "RH2M"), harvest, lambda r: r["RH2M"] >= 85 and 15 <= r["T2M"] <= 25)),
    ("harvest_dew_days", None, dew_days),
    # 토양
    ("topsoil_moisture", None, agg("GWETTOP", gs, "mean")),
    ("soil_drought_days", None, soil_drought_days),
    ("harvest_soil_moisture", None, agg("GWETROOT", harvest, "mean")),
    ("spring_soil_moisture", None, agg("GWETROOT", spring, "mean")),
    # 햇빛·바람
    ("harvest_solar", None, agg("ALLSKY_SFC_SW_DWN", harvest, "mean")),
    ("summer_solar", None, agg("ALLSKY_SFC_SW_DWN", summer, "mean")),
    ("flowering_solar", None, agg("ALLSKY_SFC_SW_DWN", flowering, "mean")),
    ("cloudy_days_gs", None, sky_days(gs, lambda k: k < 0.4)),
    ("sunny_days_gs", None, sky_days(gs, lambda k: k >= 0.8)),
    ("gs_wind_mean", None, agg("WS2M", gs, "mean")),
    ("spring_windy_days", None, agg("WS2M", early_season, "count_ge", 5)),
    ("spring_windy_days", 4, agg("WS2M", early_season, "count_ge", 4)),
    ("spring_windy_days", 6, agg("WS2M", early_season, "count_ge", 6)),
    # 생육 시기
    ("thermal_gs_start", None, thermal_start),
    ("thermal_gs_end", None, thermal_end),
    ("thermal_gs_length", None, thermal_length),
    ("gdd_milestone_date", None, gdd_milestone(1000)),
    ("gdd_milestone_date", 800, gdd_milestone(800)),
    ("gdd_milestone_date", 1200, gdd_milestone(1200)),
    # 2차로 더한 지표
    ("greenup_frost_days", None, greenup_frost(0)),
    ("greenup_frost_days", -2, greenup_frost(-2)),
    ("radiation_frost_nights", None, multi(("T2M_MIN", "WS2M"), spring, lambda r: r["T2M_MIN"] <= 2 and r["WS2M"] < 2)),
    ("first_autumn_frost", None, first_autumn_frost(0)),
    ("first_autumn_frost", -2, first_autumn_frost(-2)),
    ("winter_cold_days", None, agg("T2M_MIN", team_winter, "count_le", -10)),
    ("winter_cold_days", -5, agg("T2M_MIN", team_winter, "count_le", -5)),
    ("winter_cold_days", -15, agg("T2M_MIN", team_winter, "count_le", -15)),
    ("winter_cold_days", -20, agg("T2M_MIN", team_winter, "count_le", -20)),
    ("chill_days", None, multi(("T2M",), dormancy, lambda r: 0 < r["T2M"] <= 7.2)),
    ("heat_spell_max", None, longest_run("T2M_MAX", gs, lambda v: v >= 35)),
    ("heat_spell_max", 30, longest_run("T2M_MAX", gs, lambda v: v >= 30)),
    ("spring_mean_temp", None, agg("T2M", spring3, "mean")),
    ("flowering_temp", None, agg("T2M", flowering, "mean")),
    ("flowering_rain", None, agg("PRECTOTCORR", flowering, "sum")),
    ("downy_mildew_days", None, multi(("T2M", "PRECTOTCORR"), early_season, lambda r: r["T2M"] >= 10 and r["PRECTOTCORR"] >= 10)),
    ("powdery_mildew_days", None, multi(("T2M", "T2M_MAX"), gs, lambda r: 21 <= r["T2M"] <= 30 and r["T2M_MAX"] < 35)),
    ("max_daily_rain", None, max_of("PRECTOTCORR", gs)),
    ("winter_rain", None, agg("PRECTOTCORR", dormancy, "sum")),
    ("vpd_mean", None, vpd_mean),
    ("water_balance", None, water_balance),
    ("ripening_dtr", None, dtr_in(harvest)),
    # 1차로 더한 지표
    # 새 지표
    ("gst_mean", None, agg("T2M", gs, "mean")),
    ("bedd", None, bedd),
    ("dtr_growing", None, dtr),
    ("ripening_temp", None, agg("T2M", harvest, "mean")),
    ("gs_solar", None, agg("ALLSKY_SFC_SW_DWN", gs, "mean")),
    ("spring_frost_min", None, agg("T2M_MIN", spring, "min")),
    ("tropical_nights", None, agg("T2M_MIN", gs, "count_ge", 20)),
    ("tropical_nights", 18, agg("T2M_MIN", gs, "count_ge", 18)),
    ("tropical_nights", 22, agg("T2M_MIN", gs, "count_ge", 22)),
    ("gs_rain_total", None, agg("PRECTOTCORR", gs, "sum")),
    ("gs_wet_days", None, agg("PRECTOTCORR", gs, "count_ge", 1)),
    ("gs_wet_days", 5, agg("PRECTOTCORR", gs, "count_ge", 5)),
    ("gs_wet_days", 10, agg("PRECTOTCORR", gs, "count_ge", 10)),
    ("dry_spell_max", None, dry_spell),
    ("harvest_humidity", None, agg("RH2M", harvest, "mean")),
    ("last_spring_frost", None, last_spring_frost(0)),
    ("last_spring_frost", -2, last_spring_frost(-2)),
    ("frost_free_days", None, frost_free(0)),
    # 팀 지표의 추가 기준값 (정의는 팀과 같음)
    ("frost_after_budburst", -1, agg("T2M_MIN", spring, "count_le", -1)),
    ("frost_after_budburst", -3, agg("T2M_MIN", spring, "count_le", -3)),
    ("heat_days", 32, agg("T2M_MAX", gs, "count_ge", 32)),
    ("heat_days", 38, agg("T2M_MAX", gs, "count_ge", 38)),
    ("harvest_rain_days", 10, agg("PRECTOTCORR", harvest, "count_ge", 10)),
    ("harvest_rain_days", 30, agg("PRECTOTCORR", harvest, "count_ge", 30)),
]


def check_team_definitions(daily: dict, wb) -> None:
    """팀이 계산한 연도별 값을 일별 자료로 다시 계산해 정의가 같은지 확인합니다."""
    header, rows = rows_of(wb, "7_연도별지표")
    checks = {
        "생육기 적산온도 GDD(기준10°C)": lambda D, y, s: (lambda w: None if w is None else round(sum(max(0, v - 10) for _, v in w), 1))(window(D, *gs(y, s), "T2M")),
        "폭염일수(Tmax≥35°C)": agg("T2M_MAX", gs, "count_ge", 35),
        "고온일수(Tmax≥30°C)": agg("T2M_MAX", gs, "count_ge", 30),
        "서늘한 밤 지수": agg("T2M_MIN", lambda y, s: (date(y, 3, 1), date(y, 3, 31)) if s else (date(y, 9, 1), date(y, 9, 30)), "mean"),
        "수확기 강수량": agg("PRECTOTCORR", harvest, "sum"),
        "수확기 호우일수(≥20mm)": agg("PRECTOTCORR", harvest, "count_ge", 20),
        "생육기 뿌리층 토양수분": lambda D, y, s: (lambda w: None if w is None else round(sum(v for _, v in w) / len(w), 3))(window(D, *gs(y, s), "GWETROOT")),
        "봄 서리일수(Tmin≤0°C)": agg("T2M_MIN", spring, "count_le", 0),
        "봄 강한서리일수(Tmin≤−2°C)": agg("T2M_MIN", spring, "count_le", -2),
    }
    bad = {}
    total = {}
    for r in rows:
        rec = dict(zip(header, r))
        region = rec["산지"]
        for col, fn in checks.items():
            want = num(rec[col])
            if want is None:
                continue
            if region in SOUTH and col.startswith("봄"):
                continue  # 팀은 남반구 봄 서리를 같은 해 10~11월로 표기 (값은 모두 0)
            got = fn(daily[region], int(rec["연도"]), region in SOUTH)
            total[col] = total.get(col, 0) + 1
            if got is None or abs(got - want) > max(0.06, abs(want) * 0.001):
                bad.setdefault(col, []).append((region, rec["연도"], want, got))
    for col in checks:
        n_bad = len(bad.get(col, []))
        print(f"  정의 확인 {col}: {total.get(col, 0) - n_bad}/{total.get(col, 0)} 일치" + (f"  예: {bad[col][:2]}" if n_bad else ""))


def rows_of(wb, name):
    it = wb[name].iter_rows(values_only=True)
    header = next(it)
    return header, [r for r in it if r and r[0] is not None]


def main(xlsx: str) -> None:
    wb = openpyxl.load_workbook(xlsx, read_only=True, data_only=True)
    store: dict = {}

    def put(var_id, region, thr, year, value):
        v = num(value)
        if v is None:
            return
        store.setdefault((var_id, REGION_MAP[region], thr), {})[int(year)] = v

    header, rows = rows_of(wb, "7_연도별지표")
    unknown = [h for h in header[2:] if h not in COLUMN_MAP]
    if unknown:
        raise SystemExit(f"7_연도별지표에 매핑되지 않은 열이 있습니다: {unknown}")
    for r in rows:
        rec = dict(zip(header, r))
        for col, (var_id, thr) in COLUMN_MAP.items():
            put(var_id, rec["산지"], thr, rec["연도"], rec[col])

    _, rows = rows_of(wb, "15_전전A_MODIS연도별")
    for r in rows:
        put("spring_night_lst", r[0], None, r[1], r[2])
        put("modis_cold_periods", r[0], None, r[1], r[3])

    _, rows = rows_of(wb, "8_MODIS그린업")
    for r in rows:
        put("greenup_doy", r[0], None, r[1], r[3])

    # 일별 원자료(D_ 시트)로 새 지표와 추가 기준값 계산
    daily = {region: read_daily(wb, region) for region in REGION_MAP}
    check_team_definitions(daily, wb)
    lat = {r["id"]: r["lat"] for r in json.loads((ROOT / "data" / "regions.json").read_text(encoding="utf-8"))}
    greenup: dict = {}
    for r in rows_of(wb, "8_MODIS그린업")[1]:
        if r[2]:
            greenup.setdefault(r[0], {})[int(r[1])] = date.fromisoformat(str(r[2])[:10])
    for region, D in daily.items():
        south = region in SOUTH
        CTX["lat"] = lat[REGION_MAP[region]]
        CTX["greenup"] = greenup.get(region, {})
        base = []
        for y in range(2001, 2011):
            w = window(D, *gs(y, south), "GWETROOT")
            base += [v for _, v in (w or [])]
        CTX["soil_p20"] = sorted(base)[int(0.2 * len(base))] if base else None
        for var_id, thr, fn in DERIVED:
            # 값이 하나도 없어도(예: 서리가 없는 산지) 빈 파일을 남겨 '집계 없음'과 '해당 연도 없음'을 구분
            store.setdefault((var_id, REGION_MAP[region], thr), {})
            for y in range(2001, 2027):
                v = fn(D, y, south)
                if v is not None:
                    put(var_id, region, thr, y, v)

    n = write_series(store)

    # 체계적으로 만든 지표 묶음 (월·계절 통계, 평년 대비 극값, ETCCDI) → 산지별 넓은 CSV 하나 + 메타데이터 JSON
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import generate_families as gf

    metas, values = gf.build(
        {REGION_MAP[r]: D for r, D in daily.items()},
        {REGION_MAP[r]: r in SOUTH for r in daily},
        {REGION_MAP[r]: lat[REGION_MAP[r]] for r in daily},
    )
    out_dir = ROOT / "data" / "series_generated"
    out_dir.mkdir(parents=True, exist_ok=True)
    ids = [m["id"] for m in metas]
    for rid, table in values.items():
        with (out_dir / f"{rid}.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["year"] + ids)
            for y in range(2001, 2027):
                row = [table.get(i, {}).get(y, "") for i in ids]
                w.writerow([y] + [("" if v == "" else (int(v) if float(v).is_integer() else v)) for v in row])
    (ROOT / "data" / "indicators_generated.json").write_text(json.dumps(metas, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    fam: dict = {}
    for m in metas:
        fam[m["family"]] = fam.get(m["family"], 0) + 1
    print(f"자동 생성 지표 {len(metas)}개 {fam}")

    # 지상 관측소·MODIS 검증 요약 (산지 정보 카드와 인사이트 '얼마나 믿을 수 있나'에 사용)
    validation = {}
    _, rows = rows_of(wb, "11_전전C_관측소오차")
    for r in rows:
        validation.setdefault(REGION_MAP[r[0]], {})["station"] = {
            "id": r[1],
            "days": int(r[2]),
            "tmin_bias": num(r[3]),
            "tmin_corr": num(r[4]),
            "tmax_bias": num(r[5]),
            "tmax_corr": num(r[6]),
        }
    _, rows = rows_of(wb, "14_전전A_MODIS요약")
    for r in rows:
        validation.setdefault(REGION_MAP[r[0]], {})["modis"] = {
            "periods": int(r[1]),
            "lst_minus_grid_tmin": num(r[2]),
            "pixel_spread_mean": num(r[3]),
            "pixel_spread_max": num(r[4]),
            "cold_pixel_periods": int(r[5]),
            "grid_cold_periods": int(r[6]),
        }
    (ROOT / "data" / "validation.json").write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # 팀이 계산한 추세 검정 결과 → 엔진 대조 테스트 기준값
    header, rows = rows_of(wb, "6_추세검정결과")
    fixture = ROOT / "tests" / "fixtures" / "team_trend_results.csv"
    fixture.parent.mkdir(parents=True, exist_ok=True)
    with fixture.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["region", "variable", "threshold", "start", "end", "n", "sen_per_decade", "mk_p", "ols_per_decade", "ols_ci_low", "ols_ci_high", "t_p"])
        for r in rows:
            var_id, thr = COLUMN_MAP[r[1]]
            start, end = str(r[3]).replace("–", "-").split("-")
            ci = [float(x) for x in str(r[11]).strip("[]").split(",")]
            w.writerow([REGION_MAP[r[0]], var_id, "" if thr is None else thr, start, end, r[4], r[6], "" if r[8] is None else r[8], r[10], ci[0], ci[1], r[12]])

    print(f"시계열 CSV {n}개, 검증 {len(validation)}개 산지, 대조 기준 {len(rows)}행을 썼습니다.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
