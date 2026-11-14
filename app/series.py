"""연도별 시계열 공급.

1) data/series/<변수id>/<산지id>.csv 가 있으면 그 값을 씁니다 (팀이 NASA 자료로 집계한 실제 값).
   기준값이 기본과 다르면 <산지id>__t<기준값>.csv 를 찾습니다 (예: frost_after_budburst/burgundy__t-2.csv).
2) 실제 값이 아예 없는 지표(지금은 연기 지표 2개)만 결정론적 예시 데이터(목업)를 만들고,
   화면에 '예시 데이터' 배지가 붙습니다.

CSV 형식:  year,value   (헤더 한 줄, 시즌은 수확 연도 기준)
팀 엑셀에서 다시 만들 때: scripts/import_team_xlsx.py
"""

from __future__ import annotations

import csv
import math
import zlib
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Optional

import numpy as np

from .catalog import DATA_DIR, DATA_END_YEAR
from .catalog import has_real_data as catalog_has_real_data

SERIES_DIR = DATA_DIR / "series"
FIRST_YEAR = 1981


class SeriesUnavailable(LookupError):
    pass


# 실제 집계가 아직 없는 지표의 예시 데이터 설정: (기본값, 10년당 변화, 잡음 표준편차, {연도: 더할 값})
# 실제 관측이 아닙니다. 산불이 컸던 해(2017·2018·2020·2021·2023)를 대략 반영해 시연이 되도록만 골랐습니다.
PROFILES: dict = {
    "harvest_smoke_days": {
        "napa": (1.5, 2.0, 1.2, {2015: 3, 2017: 8, 2018: 6, 2020: 18, 2021: 5, 2024: 4}),
        "okanagan": (1.0, 1.8, 1.0, {2015: 3, 2017: 7, 2018: 8, 2021: 9, 2023: 10}),
        "bordeaux": (0.4, 0.0, 0.5, {2022: 3}),
        "burgundy": (0.4, 0.0, 0.5, {2003: 2, 2022: 2}),
        "mosel": (0.3, 0.0, 0.4, {2022: 1}),
        "barossa": (1.0, 0.3, 0.8, {2007: 3, 2015: 2, 2020: 9}),
        "yeongdong": (0.8, 0.1, 0.6, {2019: 2}),
    },
    "harvest_aerosol_days": {
        "napa": (2.0, 1.6, 1.2, {2017: 6, 2018: 5, 2020: 15, 2021: 5}),
        "okanagan": (1.5, 1.5, 1.0, {2017: 6, 2018: 7, 2021: 8, 2023: 9}),
        "bordeaux": (1.0, 0.0, 0.7, {2022: 3}),
        "burgundy": (1.0, 0.0, 0.7, {2022: 2}),
        "mosel": (0.8, 0.0, 0.6, {}),
        "barossa": (1.5, 0.2, 0.9, {2020: 8}),
        "yeongdong": (3.0, -0.3, 1.2, {2015: 3, 2016: 2}),
    },
}

# 예시 데이터에서 기준값을 엄격하게 바꿀수록 날수가 줄어드는 정도 (목업 전용 근사)
THRESHOLD_EFFECT = {
    # 변수: (기준값이 '커질수록' 엄격해지면 +1, 단위당 감소율)
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


def _thr_name(threshold) -> str:
    return f"{float(threshold):g}"


def real_series_path(var_id: str, region_id: str, threshold=None, default_threshold=None) -> Optional[Path]:
    base = SERIES_DIR / var_id
    if threshold is not None and default_threshold is not None and float(threshold) != float(default_threshold):
        p = base / f"{region_id}__t{_thr_name(threshold)}.csv"
        return p if p.exists() else None
    p = base / f"{region_id}.csv"
    return p if p.exists() else None


has_real_data = catalog_has_real_data

GENERATED_DIR = DATA_DIR / "series_generated"


@lru_cache(maxsize=16)
def _wide(region_id: str, mtime: int) -> dict:
    """data/series_generated/<산지>.csv (year + 지표 열 수백 개) → {지표id: {연도: 값}}"""
    out: dict = {}
    with (GENERATED_DIR / f"{region_id}.csv").open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            y = int(row.pop("year"))
            for k, v in row.items():
                if v != "":
                    out.setdefault(k, {})[y] = float(v)
    return out


def generated_values(var_id: str, region_id: str) -> Optional[dict]:
    p = GENERATED_DIR / f"{region_id}.csv"
    if not p.exists():
        return None
    return _wide(region_id, p.stat().st_mtime_ns).get(var_id)


def mock_values(var_id: str, region_id: str, aggregation: str, threshold=None, default_threshold=None) -> dict:
    """1981~마지막 연도의 예시 값. 같은 입력이면 항상 같은 값."""
    prof = PROFILES.get(var_id, {}).get(region_id)
    if prof is None:
        rng0 = np.random.RandomState(_seed("default", var_id, region_id))
        prof = (float(rng0.uniform(1, 4)), float(rng0.uniform(-0.5, 0.5)), 1.0, {})
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
        notes.append(f"{meta.get('dataset')} data starts with the {meta['start_year']} season, so the analysis starts in {first}.")
    if last != end:
        notes.append(f"Data runs through the {DATA_END_YEAR} season.")

    if meta.get("family", "core") != "core":
        data = generated_values(var_id, region_id)
        if data is None:
            raise SeriesUnavailable(f"{meta['name']}: no values for this region.")
        years = [y for y in range(first, last + 1) if y in data]
        missing = (last - first + 1) - len(years)
        if missing:
            gaps = [y for y in range(first, last + 1) if y not in data]
            notes.append(f"Excluded {missing} year(s) that could not be computed ({', '.join(map(str, gaps[:5]))}{', …' if len(gaps) > 5 else ''}).")
        return SeriesResult(years, [data[y] for y in years], False, "Computed from NASA POWER daily data (auto-generated indicator)", notes)

    path = real_series_path(var_id, region_id, thr, default_thr)
    if path is not None:
        data = _read_csv(path)
        years = [y for y in range(first, last + 1) if y in data]
        missing = (last - first + 1) - len(years)
        if missing:
            gaps = [y for y in range(first, last + 1) if y not in data]
            shown = ", ".join(map(str, gaps[:5])) + (", …" if len(gaps) > 5 else "")
            notes.append(f"Excluded {missing} year(s) missing from the aggregated data ({shown}).")
        return SeriesResult(years, [data[y] for y in years], False, f"NASA {meta.get('dataset')}, team-aggregated ({path.parent.name}/{path.name})", notes)

    if has_real_data(var_id):
        # 실제 집계가 있는 지표인데 이 산지·기준값만 없으면 지어내지 않고 알립니다.
        what = f"threshold {_thr_name(thr)}{meta.get('threshold_unit') or ''}" if thr != default_thr else "this region"
        raise SeriesUnavailable(f"{meta['name']}: no real data yet for {what}.")

    data = mock_values(var_id, region_id, meta.get("aggregation", "count"), thr, default_thr)
    years = list(range(first, last + 1))
    return SeriesResult(years, [data[y] for y in years], True, "Sample data (mock-up, not real observations)", notes)
