"""LLM 호출 래퍼 (OpenAI 또는 Claude).

- VINUS_LLM_PROVIDER=openai|anthropic. 비워 두면 OPENAI_API_KEY 가 있으면 openai, 아니면 anthropic.
- 키가 없거나 VINUS_AI_DISABLED=1 이면 호출하지 않고 LLMUnavailable 을 던집니다.
  호출하는 쪽(변수 담기·인사이트)은 이걸 잡아서 규칙 기반 폴백으로 답합니다.
- 응답은 구조화 출력(JSON 스키마, strict)으로 받습니다.
"""

from __future__ import annotations

import json
import logging
import os
from typing import Optional

log = logging.getLogger("vinus.llm")

DEFAULT_ANTHROPIC_MODEL = "claude-opus-5-5"
DEFAULT_OPENAI_MODEL = "gpt-5.4-mini"


class LLMUnavailable(Exception):
    pass


def _truthy(name: str) -> bool:
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "on"}


def provider() -> str:
    p = os.getenv("VINUS_LLM_PROVIDER", "").strip().lower()
    if p in ("openai", "anthropic"):
        return p
    return "openai" if os.getenv("OPENAI_API_KEY") else "anthropic"


def model() -> str:
    if provider() == "openai":
        return os.getenv("VINUS_OPENAI_MODEL", DEFAULT_OPENAI_MODEL)
    return os.getenv("VINUS_LLM_MODEL", DEFAULT_ANTHROPIC_MODEL)


def status() -> dict:
    base = {"provider": provider(), "model": model()}
    if _truthy("VINUS_AI_DISABLED"):
        return {**base, "enabled": False, "reason": "turned off with VINUS_AI_DISABLED"}
    if provider() == "openai":
        try:
            import openai  # noqa: F401
        except ImportError:
            return {**base, "enabled": False, "reason": "openai package not installed"}
        if not os.getenv("OPENAI_API_KEY"):
            return {**base, "enabled": False, "reason": "OPENAI_API_KEY not set"}
        return {**base, "enabled": True, "reason": ""}
    try:
        import anthropic  # noqa: F401
    except ImportError:
        return {**base, "enabled": False, "reason": "anthropic package not installed (needs Python 3.10+)"}
    if not (os.getenv("ANTHROPIC_API_KEY") or os.getenv("ANTHROPIC_AUTH_TOKEN") or _truthy("VINUS_AI_FORCE")):
        return {**base, "enabled": False, "reason": "ANTHROPIC_API_KEY not set"}
    return {**base, "enabled": True, "reason": ""}


def structured_call(system: str, messages: list, schema: dict, effort: str = "low", max_tokens: int = 16000) -> dict:
    st = status()
    if not st["enabled"]:
        raise LLMUnavailable(st["reason"])
    if st["provider"] == "openai":
        return _openai_call(system, messages, schema, effort, max_tokens)
    return _anthropic_call(system, messages, schema, effort, max_tokens)


# ---------------------------------------------------------------------------
# OpenAI
# ---------------------------------------------------------------------------


def _openai_call(system: str, messages: list, schema: dict, effort: str, max_tokens: int) -> dict:
    import openai

    client = openai.OpenAI(timeout=float(os.getenv("VINUS_LLM_TIMEOUT", "90")), max_retries=1)
    kwargs = dict(
        model=model(),
        messages=[{"role": "system", "content": system}] + messages,
        response_format={"type": "json_schema", "json_schema": {"name": "vinus_output", "schema": schema, "strict": True}},
        max_completion_tokens=max_tokens,
    )
    # GPT-5·o 계열은 추론 깊이를 고를 수 있습니다 (변수 담기는 low, 인사이트는 medium).
    if model().startswith(("gpt-5", "o")):
        kwargs["reasoning_effort"] = effort
    try:
        try:
            resp = client.chat.completions.create(**kwargs)
        except openai.BadRequestError as e:
            if "reasoning_effort" in str(e) and "reasoning_effort" in kwargs:
                kwargs.pop("reasoning_effort")
                resp = client.chat.completions.create(**kwargs)
            else:
                raise
    except openai.AuthenticationError as e:
        raise LLMUnavailable("invalid OpenAI API key") from e
    except openai.RateLimitError as e:
        raise LLMUnavailable("rate limit reached or out of credits") from e
    except openai.BadRequestError as e:
        log.error("OpenAI 400: %s", e)
        raise LLMUnavailable("bad request (see server log)") from e
    except openai.APIStatusError as e:
        log.error("OpenAI API %s: %s", e.status_code, e)
        raise LLMUnavailable(f"API error {e.status_code}") from e
    except openai.APIConnectionError as e:
        raise LLMUnavailable("network error") from e

    choice = resp.choices[0]
    if getattr(choice.message, "refusal", None):
        raise LLMUnavailable("the model declined to answer")
    if choice.finish_reason == "length":
        raise LLMUnavailable("the response hit the length limit")
    text: Optional[str] = choice.message.content
    if not text:
        raise LLMUnavailable("empty response")
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise LLMUnavailable("could not parse JSON") from e


# ---------------------------------------------------------------------------
# Claude
# ---------------------------------------------------------------------------


def _anthropic_call(system: str, messages: list, schema: dict, effort: str, max_tokens: int) -> dict:
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
            # 안전 분류기가 거절하면 서버 측 대체 모델이 같은 요청을 이어받습니다.
            resp = client.beta.messages.create(**kwargs, betas=["server-side-fallback-2026-07-01"], fallbacks="default")
    except anthropic.AuthenticationError as e:
        raise LLMUnavailable("invalid API key") from e
    except anthropic.RateLimitError as e:
        raise LLMUnavailable("rate limit reached") from e
    except anthropic.BadRequestError as e:
        log.error("Claude 400: %s", e.message)
        raise LLMUnavailable("bad request (see server log)") from e
    except anthropic.APIStatusError as e:
        log.error("Claude API %s: %s", e.status_code, e.message)
        raise LLMUnavailable(f"API error {e.status_code}") from e
    except anthropic.APIConnectionError as e:
        raise LLMUnavailable("network error") from e

    if resp.stop_reason == "refusal":
        raise LLMUnavailable("the model declined to answer")
    if resp.stop_reason == "max_tokens":
        raise LLMUnavailable("the response hit the length limit")
    text: Optional[str] = next((b.text for b in resp.content if b.type == "text"), None)
    if not text:
        raise LLMUnavailable("empty response")
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise LLMUnavailable("could not parse JSON") from e
