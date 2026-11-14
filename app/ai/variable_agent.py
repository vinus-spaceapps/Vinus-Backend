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


SYSTEM_RULES = """너는 와인 생산자가 NASA 위성·모델 데이터로 기후 추세를 확인하는 웹 툴의 '변수 담기 도우미'다.
사용자가 걱정이나 궁금한 점을 말하면, 아래 [변수 목록]에서 관련 변수를 골라 분석 바구니에 담아 준다.

규칙:
1. [변수 목록]에 있는 변수만 추천한다. 목록에 없는 변수를 지어내지 않는다. 맞는 변수가 없으면 없다고 말하고 가장 가까운 것을 제안한다.
2. 한 번에 최대 3개까지 담는다. 각 변수마다 왜 관련 있는지 이유를 한 줄로 쓴다.
3. 걱정이 모호하면(예: "날씨가 걱정돼") 담지 말고 add 를 빈 배열로 두고, 어떤 점이 걱정인지 한 번 되묻는다.
4. 변수 설명 질문("적산온도가 뭐야?")에는 [변수 목록]의 definition·why 내용으로만 답하고 add 는 빈 배열로 둔다.
5. 이미 바구니에 있는 변수는 다시 담지 않는다. 바구니는 최대 3개이므로 자리가 없으면 무엇을 빼면 좋을지 제안만 한다.
6. reply 는 생산자가 읽는 쉬운 한국어 존댓말로 2~4문장. 담았으면 "빼려면 바구니에서 ×를 누르세요"를 덧붙인다.
7. 기울기·p값 같은 분석 결과 숫자는 아직 계산 전이므로 말하지 않는다. 미래를 예측하지 않는다.
"""


def _system_prompt() -> str:
    return SYSTEM_RULES + "\n[변수 목록]\n" + json.dumps(_catalog_for_prompt(), ensure_ascii=False, indent=1)


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
    line = "(현재 분석 바구니: " + (", ".join(names) if names else "비어 있음") + f" / 최대 {BASKET_LIMIT}개, 남은 자리 {room}개)"
    if room == 0:
        line += "\n(바구니가 가득 찼다. add 는 빈 배열로 두고, 무엇을 빼면 좋을지 제안만 한다.)"
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

QUESTION_PAT = re.compile(r"(뭐야|뭔가요|무엇|뭐예요|뭐에요|뜻|설명|알려|이란|란\?|어떤 거|어떤거)")


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
            "reply": "어떤 점이 가장 걱정되세요? 예를 들어 봄 서리, 여름 폭염, 수확기 비, 산불 연기, 가뭄, 지금 품종이 계속 맞을지 같은 걸 말씀해 주시면 맞는 변수를 담아 드릴게요. "
            f"직접 고르시려면 왼쪽 카테고리({cats})를 보세요.",
            "add": [],
        }

    picks = [{"id": m["id"], "reason": m.get("short", "")} for m in hits[:MAX_ADD]]
    out = _sanitize({"add": picks}, req.basket)
    if not out["add"]:
        if len(req.basket) >= BASKET_LIMIT:
            return {"reply": f"바구니가 가득 찼어요(최대 {BASKET_LIMIT}개). {hits[0]['name']}을(를) 보려면 바구니에서 하나를 빼 주세요.", "add": []}
        return {"reply": f"{hits[0]['name']}은(는) 이미 바구니에 있어요. 다음 단계에서 지역을 고르시면 됩니다.", "add": []}
    names = ", ".join(a["name"] for a in out["add"])
    lines = [f"{names}을(를) 담았어요."] + [f"· {a['name']}: {a['reason']}" for a in out["add"]]
    lines.append("빼려면 바구니에서 ×를 누르세요.")
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
            result["reply"] += f"\n\n※ 바구니가 가득 차서({BASKET_LIMIT}개) {names}은(는) 담지 못했어요. 하나를 빼고 다시 말씀해 주세요."
        result["source"] = "llm"
        return result
    except llm.LLMUnavailable as e:
        result = fallback_reply(req)
        result["source"] = "fallback"
        result["fallback_reason"] = str(e)
        return result
