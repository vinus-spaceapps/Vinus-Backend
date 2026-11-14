"""① 변수 고르기의 '변수 담기 AI'.

출력: {"reply": "...", "add": [{"id": "...", "reason": "..."}]}
- 목록에 있는 변수만 추천 (스키마 enum 으로 강제 + 서버 검증)
- 한 번에 최대 3개, 각각 이유 한 줄
- 걱정이 모호하면 추천 전에 되묻기
"""

from __future__ import annotations

import json
import re
from typing import List

from pydantic import BaseModel, Field

from .. import catalog
from . import llm

MAX_ADD = 3
BASKET_LIMIT = 3


class ChatMessage(BaseModel):
    role: str = Field(..., pattern="^(user|assistant)$")
    content: str = Field(..., max_length=2000)


class VariableChatRequest(BaseModel):
    messages: List[ChatMessage] = Field(..., min_length=1, max_length=30)
    basket: List[str] = Field(default_factory=list)


def _core() -> list:
    """AI 에게는 사람이 쓴 핵심 지표만 보여 줍니다 (자동 생성 지표 수백 개는 프롬프트에 넣지 않음)."""
    return [m for m in catalog.indicators().values() if m.get("family", "core") == "core"]


def _catalog_for_prompt() -> list:
    return [
        {
            "id": m["id"],
            "name": m["name"],
            "category": next(c["name"] for c in catalog.CATEGORIES if c["id"] == m["category"]),
            "short": m.get("short", ""),
            "stage": m.get("stage", ""),
            "dataset": m.get("dataset", ""),
            "definition": m["sections"].get("definition", ""),
            "why": m["sections"].get("why", ""),
            "keywords": m["keywords"],
        }
        for m in _core()
    ]


SYSTEM_RULES = """You are the "indicator picker" assistant in a web tool where wine growers check climate trends in their region with NASA satellite and model data.
When the user describes a worry or question, pick the relevant indicators from [INDICATORS] below and add them to the analysis basket.

Rules:
1. Recommend only indicators listed in [INDICATORS]. Never invent one. If nothing fits, say so and suggest the closest one.
2. Add at most 3 at a time, each with a one-line reason why it is relevant.
3. If the worry is vague (e.g. "I'm worried about the weather"), add nothing (empty add array) and ask once what exactly worries them.
4. For questions about what an indicator means ("What is GDD?"), answer only from that indicator's definition and why in [INDICATORS], with an empty add array.
5. Never re-add an indicator already in the basket. The basket holds at most 3; if it is full, only suggest what to remove.
6. Write reply in plain, friendly English for a grower, 2–4 sentences, even if the user writes in another language. If you added indicators, end with "To remove one, click × in the basket."
7. Do not state analysis numbers such as slopes or p-values (nothing has been computed yet). Do not predict the future.
"""


def _system_prompt() -> str:
    return SYSTEM_RULES + "\n[INDICATORS]\n" + json.dumps(_catalog_for_prompt(), ensure_ascii=False, indent=1)


def _schema() -> dict:
    ids = [m["id"] for m in _core()]
    return {
        "type": "object",
        "properties": {
            "reply": {"type": "string"},
            "add": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {"id": {"type": "string", "enum": ids}, "reason": {"type": "string"}},
                    "required": ["id", "reason"],
                    "additionalProperties": False,
                },
            },
        },
        "required": ["reply", "add"],
        "additionalProperties": False,
    }


def _basket_line(basket: List[str]) -> str:
    names = [f"{catalog.indicator(b)['name']}({b})" for b in basket if catalog.indicator(b)]
    room = max(0, BASKET_LIMIT - len(basket))
    line = "(Current basket: " + (", ".join(names) if names else "empty") + f" / max {BASKET_LIMIT}, {room} slot(s) left)"
    if room == 0:
        line += "\n(The basket is full. Leave add empty and only suggest what to remove.)"
    return line


def _sanitize(out: dict, basket: List[str]) -> dict:
    seen = set(basket)
    room = max(0, BASKET_LIMIT - len(basket))
    add = []
    for item in out.get("add", []):
        vid = item.get("id")
        if vid in seen or catalog.indicator(vid) is None:
            continue
        seen.add(vid)
        add.append({"id": vid, "name": catalog.indicator(vid)["name"], "reason": str(item.get("reason", ""))[:200]})
    return {"reply": str(out.get("reply", "")).strip(), "add": add[: min(MAX_ADD, room)]}


# ---------------------------------------------------------------------------
# 규칙 기반 폴백 (AI 꺼짐·키 없음·API 오류)
# ---------------------------------------------------------------------------

QUESTION_PAT = re.compile(r"(\bwhat\b|\bmean|\bexplain|\bdefine|\bhow does|뭐야|뭔가요|무엇|뜻|설명|알려|이란)", re.I)


def _score(meta: dict, text: str) -> int:
    t = text.lower()
    score = 0
    if meta["name"] in text:
        score += 5
    for kw in meta["keywords"]:
        if str(kw).lower() in t:
            score += 2 if len(str(kw)) >= 2 else 1
    return score


def fallback_reply(req: VariableChatRequest) -> dict:
    text = req.messages[-1].content
    # 핵심 지표를 먼저 추천 (자동 생성 지표는 같은 점수면 뒤로)
    scored = sorted(((_score(m, text) + (3 if m.get("family", "core") == "core" else 0) * (_score(m, text) > 0), m) for m in catalog.indicators().values()), key=lambda x: -x[0])
    hits = [m for s, m in scored if s > 0]

    if hits and QUESTION_PAT.search(text):
        m = hits[0]
        reply = f"{m['name']}: {m['sections'].get('definition', m.get('short', ''))}\n{m['sections'].get('why', '')}"
        return {"reply": reply.strip(), "add": []}

    if not hits:
        cats = " / ".join(c["name"] for c in catalog.CATEGORIES)
        return {
            "reply": "What worries you most? For example spring frost, summer heat, harvest rain, wildfire smoke, drought, or whether your varieties will still suit the region — tell me and I'll add matching indicators. "
            f"To pick them yourself, browse the categories ({cats}).",
            "add": [],
        }

    picks = [{"id": m["id"], "reason": m.get("short", "")} for m in hits[:MAX_ADD]]
    out = _sanitize({"add": picks}, req.basket)
    if not out["add"]:
        if len(req.basket) >= BASKET_LIMIT:
            return {"reply": f"Your basket is full (max {BASKET_LIMIT}). Remove one to look at {hits[0]['name']}.", "add": []}
        return {"reply": f"{hits[0]['name']} is already in your basket. Pick a region in the next step.", "add": []}
    names = ", ".join(a["name"] for a in out["add"])
    lines = [f"Added {names}."] + [f"· {a['name']}: {a['reason']}" for a in out["add"]]
    lines.append("To remove one, click × in the basket.")
    out["reply"] = "\n".join(lines)
    return out


def reply(req: VariableChatRequest) -> dict:
    history = [{"role": m.role, "content": m.content} for m in req.messages[-12:]]
    while history and history[0]["role"] != "user":
        history.pop(0)
    history[-1] = {"role": "user", "content": f"{_basket_line(req.basket)}\n\n{history[-1]['content']}"}
    try:
        out = llm.structured_call(_system_prompt(), history, _schema(), effort="low")
        result = _sanitize(out, req.basket)
        wanted = [a.get("id") for a in out.get("add", []) if a.get("id") not in req.basket]
        if wanted and not result["add"]:
            # 모델이 담겠다고 했지만 자리가 없어 실제로는 못 담은 경우 — 답변과 화면이 어긋나지 않게 밝힘
            names = ", ".join(catalog.indicator(v)["name"] for v in wanted if catalog.indicator(v))
            result["reply"] += f"\n\nNote: the basket is full ({BASKET_LIMIT}), so {names} could not be added. Remove one and ask again."
        result["source"] = "llm"
        return result
    except llm.LLMUnavailable as e:
        result = fallback_reply(req)
        result["source"] = "fallback"
        result["fallback_reason"] = str(e)
        return result
