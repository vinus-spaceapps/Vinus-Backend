"""④ 분석 페이지의 '인사이트 AI'.

엔진이 계산한 재료 묶음(build_materials)만 입력으로 받고, 6칸 인사이트 카드를 만듭니다.
결정 맥락(무엇을 고민 중인지)이 없으면 카드를 쓰기 전에 한 번 묻습니다.
"""

from __future__ import annotations

import json
import math
import re
from typing import List, Optional

from pydantic import BaseModel, Field

from .. import catalog
from ..analysis import AnalyzeRequest, build_materials, detect_sentence, run_analysis
from . import llm

DECISIONS = [
    {"id": "variety", "label": "품종 교체"},
    {"id": "frost_invest", "label": "서리 대비 투자"},
    {"id": "insurance", "label": "보험·계약"},
    {"id": "harvest", "label": "수확 계획"},
    {"id": "curious", "label": "그냥 궁금함"},
]
DECISION_IDS = [d["id"] for d in DECISIONS]

RELATED = {
    "harvest_smoke_days": "harvest_aerosol_days",
    "harvest_aerosol_days": "harvest_smoke_days",
    "frost_after_budburst": "gdd_growing_season",
    "heat_days": "ripening_night_lst",
    "ripening_night_lst": "gdd_growing_season",
    "gdd_growing_season": "heat_days",
    "harvest_rain_days": "gs_soil_moisture",
    "gs_soil_moisture": "harvest_rain_days",
}


class InsightContext(BaseModel):
    decision: Optional[str] = None
    role: Optional[str] = None


class InsightRequest(BaseModel):
    query: AnalyzeRequest
    variable_id: str
    context: InsightContext = Field(default_factory=InsightContext)
    question: Optional[str] = Field(default=None, max_length=1000)


SYSTEM_RULES = """너는 와인 생산자를 돕는 기후 추세 '인사이트 도우미'다. 사용자 메시지의 [재료] JSON 은 통계 엔진이 NASA 데이터로 미리 계산한 결과다.

반드시 지킬 규칙:
1. 숫자는 [재료]에 있는 값만 쓴다. 직접 계산하거나 새 숫자를 만들지 않는다. 필요한 값이 없으면 "계산되지 않았다"고 쓴다. 숫자는 소수 첫째 자리 정도로 반올림해 써도 된다.
2. p값은 "추세가 없을 때 이만한 변화가 우연히 나올 확률"로만 설명한다. "추세가 진짜일 확률"이라고 쓰지 않는다.
3. 원인을 단정하지 않는다. documents 에 근거가 있을 때만 "~와 관련이 있을 수 있다"고 쓰고 sources 에 그 문서 id 를 넣는다.
4. 미래를 예측하지 않는다. 관측 기간 안의 비교로만 말한다.
5. 지시하지 말고 "고려해 볼 점"으로 쓴다. 투자·보험 결정을 대신 내리지 않는다.
6. verdict.status 가 not_significant 이면 "아직 판단하기 이르다"고 쓰고 detectable 을 설명한다. detectable.status 가 need_more 면 more_years 를, length_enough 면 "기간은 충분한 편이라 실제 변화는 더 작거나 없을 수 있다"를, no_trend 면 "추정할 수 없다"를 쓴다.
7. flags 에 tests_disagree 가 있으면 t-검정과 Mann-Kendall 결과가 엇갈린다는 것을, one_year_drives_result 가 있으면 leave_out_most_extreme.year 를 빼면 판정이 바뀐다는 것을 confidence 에 반드시 밝힌다. autocorrelation_weakens 가 있으면 자기상관 보정 시 유의성이 약해진다는 것도 밝힌다.
8. 결과가 산지 단위라 밭 하나를 대표하지 않는다는 점을 confidence 에 한 줄로 밝힌다. data_is_mock 이 true 면 "예시 데이터"라는 점도 밝힌다.
9. user_context.decision 에 맞춰 meaning 을 쓴다. curious 면 일반적인 의미만 쓴다.
10. 쉬운 한국어 존댓말. 전문용어는 괄호로 풀어 쓴다. 각 칸은 2~4문장.

칸 설명:
- summary: 한 줄 요약. 무엇이, 얼마나, 얼마나 확실하게 변했나.
- numbers: 초기 vs 최근 평균(early_vs_late), 기울기와 95% 신뢰구간.
- confidence: 판정, 두 검정 p값, 튄 해 영향, 해상도 한계.
- meaning: 생산자에게 의미. 지표 문서의 해석 가이드와 고민 중인 결정에 연결한 "고려해 볼 점".
- next_steps: 다음에 확인해 볼 것 2~3개. change.type 은 threshold(값은 indicator.threshold_options 중 하나), region(값은 다른 산지 id), start_year(값은 indicator.start_year_available 이상의 연도), add_variable(값은 변수 id) 중 하나.
- sources: 참고한 문서 id (documents[].id) 와 데이터셋 이름.
"""

QUESTION_RULES = """
지금은 사용자가 자유 질문을 했다. 위 규칙 1~8, 10을 그대로 지키며 answer 에 2~6문장으로 답한다.
[재료]로 답할 수 없는 질문이면 그렇다고 말하고, 툴에서 확인해 볼 수 있는 방법(변수·지역·기간 바꾸기)을 제안한다.
"""


def _card_schema(var_ids: list, region_ids: list, source_ids: list) -> dict:
    return {
        "type": "object",
        "properties": {
            "summary": {"type": "string"},
            "numbers": {"type": "string"},
            "confidence": {"type": "string"},
            "meaning": {"type": "string"},
            "next_steps": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "label": {"type": "string"},
                        "change": {
                            "type": "object",
                            "properties": {
                                "type": {"type": "string", "enum": ["threshold", "region", "start_year", "add_variable"]},
                                "value": {"type": "string"},
                            },
                            "required": ["type", "value"],
                            "additionalProperties": False,
                        },
                    },
                    "required": ["label", "change"],
                    "additionalProperties": False,
                },
            },
            "sources": {"type": "array", "items": {"type": "string", "enum": source_ids}},
        },
        "required": ["summary", "numbers", "confidence", "meaning", "next_steps", "sources"],
        "additionalProperties": False,
    }


def _answer_schema(source_ids: list) -> dict:
    return {
        "type": "object",
        "properties": {
            "answer": {"type": "string"},
            "sources": {"type": "array", "items": {"type": "string", "enum": source_ids}},
        },
        "required": ["answer", "sources"],
        "additionalProperties": False,
    }


# ---------------------------------------------------------------------------
# 검증
# ---------------------------------------------------------------------------

NUM_RE = re.compile(r"(?<![\w.])-?\d+(?:\.\d+)?")


def _collect_numbers(obj, out: set) -> None:
    if isinstance(obj, bool) or obj is None:
        return
    if isinstance(obj, (int, float)):
        if math.isfinite(obj):
            out.add(float(obj))
        return
    if isinstance(obj, str):
        for m in NUM_RE.findall(obj):
            out.add(float(m))
        return
    if isinstance(obj, dict):
        for v in obj.values():
            _collect_numbers(v, out)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            _collect_numbers(v, out)


def unverified_numbers(texts: List[str], materials: dict) -> List[str]:
    """AI 가 쓴 숫자 중 재료에 없는 숫자. (작은 정수·서식용 숫자는 통과)"""
    allowed: set = set()
    _collect_numbers(materials, allowed)
    allowed |= {95.0, 0.05, 5.0, 10.0}
    bad = []
    for t in texts:
        for raw in NUM_RE.findall(t):
            x = float(raw)
            if abs(x) <= 10 and x == int(x):
                continue
            ok = any(abs(abs(x) - abs(a)) <= max(0.051, 0.01 * abs(a)) for a in allowed)
            if not ok:
                bad.append(raw)
    return sorted(set(bad))


def _valid_step(step: dict, m: dict) -> Optional[dict]:
    ch = step.get("change", {})
    t, v = ch.get("type"), str(ch.get("value", ""))
    ind = m["indicator"]
    if t == "threshold":
        try:
            fv = float(v)
        except ValueError:
            return None
        if not any(float(o) == fv for o in ind["threshold_options"]):
            return None
        if ind["threshold"] is not None and float(ind["threshold"]) == fv:
            return None
        value = fv
    elif t == "region":
        if catalog.region(v) is None or v == m["region"]["id"]:
            return None
        value = v
    elif t == "start_year":
        try:
            value = int(float(v))
        except ValueError:
            return None
        if not (ind["start_year_available"] <= value < m["period"]["end"] - 5):
            return None
    elif t == "add_variable":
        if catalog.indicator(v) is None or v in m.get("selected_variables", [ind["id"]]):
            return None
        value = v
    else:
        return None
    return {"label": str(step.get("label", ""))[:60], "change": {"type": t, "value": value}}


# ---------------------------------------------------------------------------
# 규칙 기반 폴백 카드
# ---------------------------------------------------------------------------


def _n(x: Optional[float], d: int = 1) -> str:
    if x is None:
        return "계산되지 않음"
    s = f"{x:+.{d}f}"
    return s


def _plain(x: Optional[float], d: int = 1) -> str:
    return "계산되지 않음" if x is None else f"{x:.{d}f}"


def _p(x: Optional[float]) -> str:
    if x is None:
        return "계산되지 않음"
    return "p < 0.001" if x < 0.001 else f"p = {x:.3f}"


DECISION_TEXT = {
    "variety": "재식재는 수십 년을 내다보는 결정이라 한 지표만으로 정하기보다, 적산온도·폭염일수·밤 기온처럼 품종 적합성에 직접 닿는 지표를 함께 보는 것을 고려해 보세요.",
    "frost_invest": "서리 대비 시설은 극단적인 해 한두 번의 피해를 막는 투자라, 추세 방향과 별개로 극단값이 얼마나 자주 나왔는지를 함께 보는 것을 고려해 보세요.",
    "insurance": "보험·계약 조건을 이야기할 때 '산지 단위에서 이런 추세가 관측된다'는 근거로 쓸 수 있지만, 밭 단위 피해의 증거는 아니라는 점을 함께 밝히는 것이 좋습니다.",
    "harvest": "수확 일정이나 인력 계획을 세울 때 오래된 평년값보다 최근 10년 평균을 기준으로 삼는 것을 고려해 보세요.",
    "curious": "",
}


def fallback_card(m: dict) -> dict:
    ind, reg, per, tr = m["indicator"], m["region"], m["period"], m["trend"]
    unit = ind["unit"]
    v = tr["verdict"]
    slope = tr["slope_per_decade"]
    lo, hi = tr["ci95_per_decade"]
    ev = m["early_vs_late"]
    lo_ext = m["leave_out_most_extreme"]
    flags = m["flags"]
    word = "늘었" if v["direction"] == "increase" else "줄었" if v["direction"] == "decrease" else "변하지 않았"

    if v["status"] == "significant":
        summary = (
            f"{reg['name']}의 {ind['name']}은(는) {per['start']}~{per['end']} 동안 10년에 {_n(slope)}{unit}씩 {word}고, "
            "우연으로 보기 어려운 수준(통계적으로 유의)입니다."
        )
    elif v["status"] == "mixed":
        summary = (
            f"{reg['name']}의 {ind['name']}은(는) {per['start']}~{per['end']} 동안 {word}는 경향이 보이지만, "
            "두 검정 결과가 엇갈려 아직 확실하다고 말하기 어렵습니다."
        )
    else:
        summary = f"{reg['name']}의 {ind['name']}은(는) {per['start']}~{per['end']} 동안 뚜렷한 추세가 확인되지 않았습니다. 아직 판단하기 이릅니다."

    numbers = (
        f"초기 {ev['early']['from']}~{ev['early']['to']} 평균 {_plain(ev['early']['mean'])}{unit} → "
        f"최근 {ev['late']['from']}~{ev['late']['to']} 평균 {_plain(ev['late']['mean'])}{unit} (차이 {_n(ev['difference'])}{unit}). "
        f"{tr['method']}은 10년에 {_n(slope)}{unit}, 95% 신뢰구간(기울기가 있을 법한 범위)은 {_n(lo)} ~ {_n(hi)}{unit}입니다."
    )

    conf = [
        f"판정: {v['label']}. t-검정 {_p(tr['p_ttest'])}, Mann-Kendall {_p(tr['p_mann_kendall'])}"
        " (p값은 추세가 없을 때 이만한 변화가 우연히 나올 확률입니다)."
    ]
    if "tests_disagree" in flags:
        conf.append("t-검정(기울기)과 Mann-Kendall(순위)의 결과가 엇갈립니다. 몇몇 해의 큰 값이 기울기를 끌어올렸을 수 있습니다.")
    if "one_year_drives_result" in flags:
        conf.append(f"가장 튄 {lo_ext['year']}년을 빼면 판정이 '{lo_ext['verdict']['label']}'(으)로 바뀝니다. 한 해가 결과를 좌우하고 있습니다.")
    else:
        conf.append(f"가장 튄 {lo_ext['year']}년을 빼도 판정은 그대로입니다.")
    if "autocorrelation_weakens" in flags:
        conf.append(f"해마다 값이 이어지는 경향(자기상관)을 보정하면 t-검정 {_p(tr['p_ttest_autocorr_adjusted'])}로 유의성이 약해집니다.")
    if v["status"] != "significant":
        conf.append(detect_sentence(tr["detectable"]) + ".")
    conf.append(m["resolution_note"])
    if m["data_is_mock"]:
        conf.append("지금 화면은 예시 데이터(목업)입니다.")
    confidence = " ".join(conf)

    bad_up = ind["higher_is"] == "worse"
    bad_down = ind["higher_is"] == "better"
    is_bad = (v["direction"] == "increase" and bad_up) or (v["direction"] == "decrease" and bad_down)
    ext_years = ", ".join(str(e["year"]) for e in m["extremes"])
    if v["status"] == "significant" and is_bad:
        meaning = f"생산자에게 불리한 쪽으로 변하고 있습니다. 극단값이 컸던 해({ext_years})의 기억이 우연만은 아닐 수 있습니다."
    elif v["status"] == "significant" and (bad_up or bad_down):
        meaning = f"위험이 줄어드는 쪽으로 변하고 있지만, 극단값이 큰 해({ext_years})는 여전히 있었습니다."
    elif v["status"] == "significant":
        meaning = "산지의 기후 조건이 꾸준히 옮겨 가고 있습니다. 좋고 나쁨은 품종과 스타일에 따라 다릅니다."
    else:
        meaning = f"장기 추세보다 해마다의 변동, 특히 극단값이 컸던 해({ext_years})에 대비하는 관점이 더 맞을 수 있습니다."
    dec = DECISION_TEXT.get((m.get("user_context") or {}).get("decision") or "curious", "")
    if dec:
        meaning += " " + dec

    steps = []
    opts = [o for o in ind["threshold_options"] if ind["threshold"] is None or float(o) != float(ind["threshold"])]
    if opts:
        steps.append({"label": f"기준을 {opts[-1]}{ind['threshold_unit']}로 바꿔 보기", "change": {"type": "threshold", "value": str(opts[-1])}})
    if m.get("nearest_region"):
        nr = m["nearest_region"]
        steps.append({"label": f"가까운 {nr['name']}와 비교", "change": {"type": "region", "value": nr["id"]}})
    rel = RELATED.get(ind["id"])
    if rel and catalog.indicator(rel):
        steps.append({"label": f"{catalog.indicator(rel)['name']}도 함께 보기", "change": {"type": "add_variable", "value": rel}})
    if per["start"] > ind["start_year_available"]:
        steps.append({"label": f"기간을 {ind['start_year_available']}년부터로 늘리기", "change": {"type": "start_year", "value": str(ind["start_year_available"])}})

    return {
        "summary": summary,
        "numbers": numbers,
        "confidence": confidence,
        "meaning": meaning,
        "next_steps": [s for s in (_valid_step(x, m) for x in steps) if s][:3],
        "sources": [m["documents"][0]["id"], ind["dataset"]],
    }


# ---------------------------------------------------------------------------
# 진입점
# ---------------------------------------------------------------------------


def _source_ids(m: dict) -> list:
    return [d["id"] for d in m["documents"]] + [m["indicator"]["dataset"]]


def respond(req: InsightRequest) -> dict:
    decision = req.context.decision if req.context.decision in DECISION_IDS else None
    if decision is None and not req.question:
        return {
            "type": "need_context",
            "question": "인사이트를 맞춰 드리려면, 지금 어떤 결정을 고민 중이세요?",
            "options": DECISIONS,
        }

    analysis = run_analysis(req.query)
    m = build_materials(analysis, req.variable_id, {"decision": decision or "curious", "role": req.context.role or "와인 생산자"})
    payload = "[재료]\n" + json.dumps(m, ensure_ascii=False)
    sources_allowed = _source_ids(m)

    if req.question:
        try:
            out = llm.structured_call(
                SYSTEM_RULES + QUESTION_RULES,
                [{"role": "user", "content": payload + "\n\n[질문]\n" + req.question}],
                _answer_schema(sources_allowed),
                effort="medium",
            )
            return {
                "type": "answer",
                "answer": out["answer"],
                "sources": [s for s in out.get("sources", []) if s in sources_allowed],
                "unverified_numbers": unverified_numbers([out["answer"]], m),
                "source": "llm",
            }
        except llm.LLMUnavailable as e:
            card = fallback_card(m)
            return {
                "type": "answer",
                "answer": "AI가 꺼져 있어 자유 질문에는 답하기 어려워요. 대신 계산된 결과를 요약해 드릴게요.\n\n" + card["summary"] + "\n" + card["confidence"],
                "sources": card["sources"],
                "unverified_numbers": [],
                "source": "fallback",
                "fallback_reason": str(e),
            }

    try:
        out = llm.structured_call(
            SYSTEM_RULES,
            [{"role": "user", "content": payload + "\n\n위 재료로 인사이트 카드를 써 줘."}],
            _card_schema(list(catalog.indicators().keys()), [r["id"] for r in catalog.regions()], sources_allowed),
            effort="medium",
        )
        steps = [s for s in (_valid_step(x, m) for x in out.get("next_steps", [])) if s][:3]
        card = {k: out[k] for k in ("summary", "numbers", "confidence", "meaning")}
        card["next_steps"] = steps or fallback_card(m)["next_steps"]
        card["sources"] = [s for s in out.get("sources", []) if s in sources_allowed] or [m["documents"][0]["id"]]
        return {
            "type": "card",
            "card": card,
            "unverified_numbers": unverified_numbers([card[k] for k in ("summary", "numbers", "confidence", "meaning")], m),
            "decision": decision,
            "source": "llm",
        }
    except llm.LLMUnavailable as e:
        return {
            "type": "card",
            "card": fallback_card(m),
            "unverified_numbers": [],
            "decision": decision,
            "source": "fallback",
            "fallback_reason": str(e),
        }
