"""Claude 호출 래퍼.

- 키가 없거나 VINUS_AI_DISABLED=1 이면 호출하지 않고 LLMUnavailable 을 던집니다.
  호출하는 쪽(변수 담기·인사이트)은 이걸 잡아서 규칙 기반 폴백으로 답합니다.
- 응답은 구조화 출력(JSON 스키마)으로 받습니다.
- 안전 분류기가 거절하면 서버 측 대체 모델(fallbacks="default")이 같은 요청을 이어받습니다.
"""

from __future__ import annotations

import json
import logging
import os
from typing import Optional

log = logging.getLogger("vinus.llm")

DEFAULT_MODEL = "claude-opus-5-5"


class LLMUnavailable(Exception):
    pass


def _truthy(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "on"}


def model() -> str:
    return os.getenv("VINUS_LLM_MODEL", DEFAULT_MODEL)


def status() -> dict:
    if _truthy("VINUS_AI_DISABLED"):
        return {"enabled": False, "model": model(), "reason": "VINUS_AI_DISABLED 로 꺼 둠"}
    try:
        import anthropic  # noqa: F401
    except ImportError:
        return {"enabled": False, "model": model(), "reason": "anthropic 패키지 없음 (Python 3.10+ 필요)"}
    if not (os.getenv("ANTHROPIC_API_KEY") or os.getenv("ANTHROPIC_AUTH_TOKEN") or _truthy("VINUS_AI_FORCE")):
        return {"enabled": False, "model": model(), "reason": "ANTHROPIC_API_KEY 없음"}
    return {"enabled": True, "model": model(), "reason": ""}


def structured_call(system: str, messages: list, schema: dict, effort: str = "low", max_tokens: int = 16000) -> dict:
    st = status()
    if not st["enabled"]:
        raise LLMUnavailable(st["reason"])

    import anthropic

    client = anthropic.Anthropic(timeout=float(os.getenv("VINUS_LLM_TIMEOUT", "90")), max_retries=1)
    kwargs = dict(
        model=model(),
        max_tokens=max_tokens,
        # 시스템 프롬프트(규칙 + 변수 목록)는 요청마다 같으므로 캐시합니다.
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=messages,
        output_config={"effort": effort, "format": {"type": "json_schema", "schema": schema}},
    )
    try:
        if _truthy("VINUS_LLM_NO_SERVER_FALLBACK"):
            resp = client.messages.create(**kwargs)
        else:
            resp = client.beta.messages.create(
                **kwargs,
                betas=["server-side-fallback-2026-07-01"],
                fallbacks="default",
            )
    except anthropic.AuthenticationError as e:
        raise LLMUnavailable("API 키가 올바르지 않습니다") from e
    except anthropic.RateLimitError as e:
        raise LLMUnavailable("요청 한도 초과") from e
    except anthropic.BadRequestError as e:
        log.error("Claude 400: %s", e.message)
        raise LLMUnavailable("잘못된 요청 (서버 로그 확인)") from e
    except anthropic.APIStatusError as e:
        log.error("Claude API %s: %s", e.status_code, e.message)
        raise LLMUnavailable(f"API 오류 {e.status_code}") from e
    except anthropic.APIConnectionError as e:
        raise LLMUnavailable("네트워크 오류") from e

    if resp.stop_reason == "refusal":
        raise LLMUnavailable("모델이 답변을 거절했습니다")
    if resp.stop_reason == "max_tokens":
        raise LLMUnavailable("응답이 길이 제한에 걸렸습니다")
    text: Optional[str] = next((b.text for b in resp.content if b.type == "text"), None)
    if not text:
        raise LLMUnavailable("빈 응답")
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise LLMUnavailable("JSON 파싱 실패") from e
