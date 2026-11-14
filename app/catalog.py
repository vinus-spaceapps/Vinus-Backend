"""지표 md·산지 목록 로더.

변수팀이 data/indicators/*.md 를 고치면 서버 재시작 없이도 다음 요청부터 반영됩니다
(파일 수정 시각이 바뀌면 다시 읽음).
"""

from __future__ import annotations

import json
import math
import re
from functools import lru_cache
from pathlib import Path
from typing import Optional

import yaml

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
INDICATOR_DIR = DATA_DIR / "indicators"

CATEGORIES = [
    {"id": "temp_frost", "name": "기온·서리"},
    {"id": "heat", "name": "더위"},
    {"id": "rain_water", "name": "비"},
    {"id": "drought", "name": "가뭄·토양"},
    {"id": "disease", "name": "병해·습도"},
    {"id": "sun_wind", "name": "햇빛·바람"},
    {"id": "smoke_air", "name": "연기·대기"},
    {"id": "growth", "name": "생육·시기"},
]

SECTION_KEYS = {
    "정의": "definition",
    "왜 중요한가": "why",
    "해석 가이드": "guide",
    "주의점": "caveats",
    "근거": "references",
}

DATA_END_YEAR = 2026


def _parse_md(text: str) -> dict:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.S)
    if not m:
        raise ValueError("frontmatter(---) 가 없습니다")
    meta = yaml.safe_load(m.group(1)) or {}
    body = m.group(2)
    sections = {}
    for chunk in re.split(r"^##\s+", body, flags=re.M)[1:]:
        title, _, content = chunk.partition("\n")
        key = SECTION_KEYS.get(title.strip(), title.strip())
        sections[key] = content.strip()
    meta["sections"] = sections
    for k in ("keywords", "threshold_options"):
        meta[k] = list(meta.get(k) or [])
    meta["robust"] = bool(meta.get("robust"))
    meta["start_year"] = int(meta.get("start_year") or 2003)
    return meta


GENERATED_FILE = DATA_DIR / "indicators_generated.json"

# 지표 묶음: core 는 사람이 쓴 지표 md, 나머지는 scripts/generate_families.py 가 만든 것
FAMILIES = [
    {"id": "core", "name": "핵심 지표"},
    {"id": "etccdi", "name": "기후 극값 지수 (ETCCDI)"},
    {"id": "extremes", "name": "평년 대비 극값 일수"},
    {"id": "stats", "name": "월·계절 기본 통계"},
]


def _dir_signature() -> tuple:
    sig = [(p.name, p.stat().st_mtime_ns) for p in INDICATOR_DIR.glob("*.md")]
    if GENERATED_FILE.exists():
        sig.append((GENERATED_FILE.name, GENERATED_FILE.stat().st_mtime_ns))
    return tuple(sorted(sig))


def _generated() -> list:
    if not GENERATED_FILE.exists():
        return []
    out = []
    for m in json.loads(GENERATED_FILE.read_text(encoding="utf-8")):
        m.setdefault("threshold", None)
        m.setdefault("threshold_unit", "")
        m.setdefault("threshold_options", [])
        m.setdefault("robust", False)
        m.setdefault("start_year", 2001)
        m["keywords"] = [k for k in m.get("keywords", []) if k]
        out.append(m)
    return out


@lru_cache(maxsize=4)
def _load_indicators(signature: tuple) -> dict:
    out = {}
    for path in sorted(INDICATOR_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        meta = _parse_md(path.read_text(encoding="utf-8"))
        if meta.get("id") != path.stem:
            raise ValueError(f"{path.name}: id({meta.get('id')}) 와 파일 이름이 다릅니다")
        meta["family"] = "core"
        out[meta["id"]] = meta
    for meta in _generated():
        if meta["id"] in out:
            raise ValueError(f"자동 생성 지표 id 가 핵심 지표와 겹칩니다: {meta['id']}")
        out[meta["id"]] = meta
    # 묶음 → 카테고리 → order → 이름 순 (핵심 지표가 먼저, 같은 카테고리끼리 묶이도록)
    fam_rank = {f["id"]: i for i, f in enumerate(FAMILIES)}
    cat_rank = {c["id"]: i for i, c in enumerate(CATEGORIES)}
    ordered = sorted(
        out.values(),
        key=lambda m: (fam_rank.get(m["family"], 99), cat_rank.get(m["category"], 99), int(m.get("order") or 99), m["name"]),
    )
    return {m["id"]: m for m in ordered}


def has_real_data(var_id: str) -> bool:
    """실제 값이 있는지: 핵심 지표는 data/series/<변수id>/, 자동 생성 지표는 data/series_generated/."""
    d = DATA_DIR / "series" / var_id
    if d.is_dir() and any(d.glob("*.csv")):
        return True
    return var_id.startswith(("m_", "s_", "x_", "etccdi_")) and any((DATA_DIR / "series_generated").glob("*.csv"))


def indicators() -> dict:
    return _load_indicators(_dir_signature())


def indicator(var_id: str) -> Optional[dict]:
    return indicators().get(var_id)


@lru_cache(maxsize=1)
def _load_regions() -> list:
    return json.loads((DATA_DIR / "regions.json").read_text(encoding="utf-8"))


def regions() -> list:
    return _load_regions()


@lru_cache(maxsize=1)
def _load_validation() -> dict:
    p = DATA_DIR / "validation.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def validation(region_id: str) -> Optional[dict]:
    """지상 관측소·MODIS 1km 와 비교한 검증 요약 (scripts/import_team_xlsx.py 가 만듦)."""
    return _load_validation().get(region_id)


def region(region_id: str) -> Optional[dict]:
    return next((r for r in regions() if r["id"] == region_id), None)


def distance_km(a: dict, b: dict) -> float:
    lat1, lon1, lat2, lon2 = map(math.radians, (a["lat"], a["lon"], b["lat"], b["lon"]))
    h = math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def nearest_region(region_id: str) -> Optional[dict]:
    me = region(region_id)
    if not me:
        return None
    others = [r for r in regions() if r["id"] != region_id]
    return min(others, key=lambda r: distance_km(me, r)) if others else None


def public_indicator(meta: dict) -> dict:
    """프론트로 내보낼 지표 정보 (hover 소개에 쓰는 내용 포함)."""
    return {
        "id": meta["id"],
        "name": meta["name"],
        "category": meta["category"],
        "short": meta.get("short", ""),
        "unit": meta.get("unit", ""),
        "dataset": meta.get("dataset", ""),
        "source": meta.get("source", ""),
        "start_year": meta["start_year"],
        "end_year": DATA_END_YEAR,
        "resolution": meta.get("resolution", ""),
        "stage": meta.get("stage", ""),
        "condition": meta.get("condition", ""),
        "threshold": meta.get("threshold"),
        "threshold_unit": meta.get("threshold_unit") or "",
        "threshold_options": meta["threshold_options"],
        "aggregation": meta.get("aggregation", "count"),
        "robust": meta["robust"],
        "higher_is": meta.get("higher_is", "neutral"),
        "station_var": meta.get("station_var"),
        "has_real_data": has_real_data(meta["id"]),
        "keywords": [str(k) for k in meta["keywords"]],
        "family": meta.get("family", "core"),
        "sections": meta["sections"],
    }
