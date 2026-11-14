"""연도별 시계열 공급.

1) data/series/<변수id>/<산지id>.csv 가 있으면 그 값을 씁니다 (팀이 Giovanni·스크립트로 집계한 실제 NASA 값).
2) 없으면 결정론적 예시 데이터(목업)를 만듭니다. 화면에 '예시 데이터' 배지가 붙습니다.

CSV 형식:  year,value   (헤더 한 줄, 시즌은 수확 연도 기준)
"""

from __future__ import annotations

import csv
import math
import zlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np

from .catalog import DATA_DIR, DATA_END_YEAR

SERIES_DIR = DATA_DIR / "series"
FIRST_YEAR = 1981

# (기본값, 10년당 변화, 잡음 표준편차, {연도: 더할 값})
# 목업이 시연 시나리오와 테스트 케이스(유의한 증가/감소, 유의하지 않음, 검정 엇갈림,
# 한 해가 결과를 좌우)를 모두 보여 주도록 값을 골랐습니다. 실제 관측이 아닙니다.
Profile = tuple

PROFILES: dict = {
    "harvest_smoke_days": {
        "rogue_valley": (1.5, 2.5, 1.2, {2015: 3, 2017: 9, 2018: 11, 2020: 17, 2021: 7, 2022: 4, 2024: 5}),
        "napa": (2.0, 0.0, 1.0, {2008: 2, 2017: 6, 2020: 22}),
        "sonoma": (2.0, 0.2, 1.0, {2017: 7, 2019: 3, 2020: 20}),
        "burgundy": (0.4, 0.0, 0.5, {2003: 2, 2019: 1, 2022: 2}),
        "mosel": (0.3, 0.0, 0.4, {2022: 1}),
        "barossa": (1.0, 0.3, 0.8, {2007: 3, 2015: 2, 2020: 9}),
        "yeongdong": (0.8, 0.1, 0.6, {2019: 2}),
    },
    "harvest_aerosol_days": {
        "rogue_valley": (2.0, 2.0, 1.2, {2017: 7, 2018: 9, 2020: 14, 2021: 6}),
        "napa": (2.5, 0.2, 1.1, {2017: 5, 2020: 16}),
        "sonoma": (2.5, 0.2, 1.1, {2017: 6, 2020: 15}),
        "burgundy": (1.0, 0.0, 0.7, {2022: 2}),
        "mosel": (0.8, 0.0, 0.6, {}),
        "barossa": (1.5, 0.2, 0.9, {2020: 8}),
        "yeongdong": (3.0, -0.3, 1.2, {2015: 3, 2016: 2}),
    },
    "frost_after_budburst": {
        "rogue_valley": (5.0, -0.9, 1.6, {2008: 3}),
        "napa": (2.0, -0.4, 1.2, {2008: 3}),
        "sonoma": (2.5, -0.5, 1.2, {2008: 3}),
        "burgundy": (4.0, -0.3, 1.8, {2016: 4, 2017: 5, 2021: 7}),
        "mosel": (6.5, -1.8, 1.2, {2017: 3}),
        "barossa": (3.0, 0.1, 1.2, {2025: 7}),
        "yeongdong": (3.0, -0.8, 1.3, {2010: 3, 2013: 2}),
    },
    "heat_days": {
        "rogue_valley": (9.0, 2.5, 3.0, {2021: 8}),
        "napa": (8.0, 2.0, 3.0, {2022: 6}),
        "sonoma": (4.0, 1.3, 2.0, {2022: 5}),
        "burgundy": (2.0, 1.4, 1.5, {2003: 9, 2019: 4, 2022: 5}),
        "mosel": (0.6, 0.6, 0.8, {2003: 4, 2019: 2}),
        "barossa": (12.0, 3.0, 3.5, {2009: 7, 2019: 8}),
        "yeongdong": (3.0, 1.5, 2.0, {2018: 9}),
    },
    "harvest_rain_days": {
        "rogue_valley": (0.8, 0.0, 0.7, {}),
        "napa": (0.3, 0.0, 0.4, {}),
        "sonoma": (0.4, 0.0, 0.4, {}),
        "burgundy": (2.0, 0.1, 1.0, {}),
        "mosel": (3.0, 0.2, 1.2, {}),
        "barossa": (0.8, -0.1, 0.6, {}),
        "yeongdong": (3.0, 0.45, 0.6, {2020: 3, 2022: 3, 2023: 4}),
    },
    "gs_soil_moisture": {
        "rogue_valley": (22.0, -0.6, 1.0, {}),
        "napa": (18.0, -0.9, 1.2, {2021: -3}),
        "sonoma": (20.0, -0.7, 1.2, {2021: -3}),
        "burgundy": (26.0, -0.5, 1.4, {2022: -3}),
        "mosel": (28.0, -0.3, 1.3, {}),
        "barossa": (15.0, -0.4, 1.3, {}),
        "yeongdong": (31.0, 0.1, 1.5, {}),
    },
    "gdd_growing_season": {
        "rogue_valley": (1500, 55, 55, {}),
        "napa": (1800, 45, 60, {}),
        "sonoma": (1600, 40, 55, {}),
        "burgundy": (1250, 70, 65, {2003: 160}),
        "mosel": (1050, 65, 55, {2018: 120}),
        "barossa": (1900, 40, 70, {}),
        "yeongdong": (1700, 50, 60, {}),
    },
    "ripening_night_lst": {
        "rogue_valley": (8.0, 0.35, 0.6, {}),
        "napa": (11.0, 0.4, 0.6, {}),
        "sonoma": (10.0, 0.35, 0.6, {}),
        "burgundy": (9.0, 0.45, 0.7, {2003: 1.5}),
        "mosel": (7.5, 0.4, 0.6, {}),
        "barossa": (12.0, 0.3, 0.7, {}),
        "yeongdong": (17.0, 0.4, 0.7, {}),
    },
}

# 기준값을 엄격하게 바꿀수록 날수가 줄어드는 정도 (목업 전용 근사)
THRESHOLD_EFFECT = {
    # 변수: (기준값이 '커질수록' 엄격해지면 +1, '작아질수록' 엄격해지면 -1, 단위당 감소율)
    "frost_after_budburst": (-1, 0.45),
    "heat_days": (+1, 0.25),
    "harvest_rain_days": (+1, 0.07),
    "harvest_smoke_days": (+1, 1.6),
    "harvest_aerosol_days": (+1, 1.2),
}


@dataclass
class SeriesResult:
    years: list
    values: list
    is_mock: bool
    source_note: str
    notes: list = field(default_factory=list)


def _seed(*parts: str) -> int:
    return zlib.crc32("|".join(parts).encode("utf-8"))


def _read_csv(path: Path) -> dict:
    out = {}
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                out[int(row["year"])] = float(row["value"])
            except (KeyError, ValueError):
                continue
    return out


def real_series_path(var_id: str, region_id: str, threshold=None, default_threshold=None) -> Optional[Path]:
    base = SERIES_DIR / var_id
    if threshold is not None and default_threshold is not None and float(threshold) != float(default_threshold):
        p = base / f"{region_id}__t{threshold}.csv"
        return p if p.exists() else None
    p = base / f"{region_id}.csv"
    return p if p.exists() else None


def mock_values(var_id: str, region_id: str, aggregation: str, threshold=None, default_threshold=None) -> dict:
    """1981~2025 전체 연도의 예시 값. 같은 입력이면 항상 같은 값."""
    prof = PROFILES.get(var_id, {}).get(region_id)
    if prof is None:
        rng0 = np.random.RandomState(_seed("default", var_id, region_id))
        prof = (float(rng0.uniform(2, 8)), float(rng0.uniform(-1, 1)), 1.5, {})
    base, trend_dec, sd, spikes = prof
    rng = np.random.RandomState(_seed(var_id, region_id))
    years = np.arange(FIRST_YEAR, DATA_END_YEAR + 1)
    noise = rng.normal(0, sd, size=years.size)
    vals = base + trend_dec * (years - 2003) / 10.0 + noise
    for y, add in spikes.items():
        if FIRST_YEAR <= y <= DATA_END_YEAR:
            vals[y - FIRST_YEAR] += add

    if aggregation == "count":
        factor = 1.0
        eff = THRESHOLD_EFFECT.get(var_id)
        if eff and threshold is not None and default_threshold is not None:
            sign, k = eff
            factor = math.exp(-k * sign * (float(threshold) - float(default_threshold)))
        vals = np.maximum(0, np.round(vals * factor))
    else:
        vals = np.round(vals, 2)
    return {int(y): float(v) for y, v in zip(years, vals)}


def get_series(meta: dict, region_id: str, start: int, end: int, threshold=None) -> SeriesResult:
    var_id = meta["id"]
    default_thr = meta.get("threshold")
    thr = default_thr if threshold is None else threshold
    notes = []

    first = max(start, meta["start_year"])
    last = min(end, DATA_END_YEAR)
    if first != start:
        notes.append(f"{meta.get('dataset')} 자료는 {meta['start_year']}년 시즌부터 있어 {first}년부터 분석했습니다.")
    if last != end:
        notes.append(f"자료는 {DATA_END_YEAR}년 시즌까지입니다.")

    path = real_series_path(var_id, region_id, thr, default_thr)
    if path is not None:
        data = _read_csv(path)
        years = [y for y in range(first, last + 1) if y in data]
        missing = (last - first + 1) - len(years)
        if missing:
            notes.append(f"집계 자료에 {missing}개 연도가 비어 있어 제외했습니다.")
        return SeriesResult(years, [data[y] for y in years], False, f"NASA {meta.get('dataset')} 집계값 ({path.name})", notes)

    if path is None and (SERIES_DIR / var_id / f"{region_id}.csv").exists() and thr != default_thr:
        notes.append("이 기준값의 실제 집계가 아직 없어 예시 데이터로 보여 줍니다.")

    data = mock_values(var_id, region_id, meta.get("aggregation", "count"), thr, default_thr)
    years = list(range(first, last + 1))
    return SeriesResult(years, [data[y] for y in years], True, "예시 데이터 (목업, 실제 관측 아님)", notes)
