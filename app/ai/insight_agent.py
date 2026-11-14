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
    {"id": "variety", "label": "Changing varieties"},
    {"id": "frost_invest", "label": "Frost protection investment"},
    {"id": "insurance", "label": "Insurance & contracts"},
    {"id": "harvest", "label": "Harvest planning"},
    {"id": "curious", "label": "Just curious"},
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


SYSTEM_RULES = """You are a climate-trend "insight assistant" for wine growers. The [MATERIALS] JSON in the user message holds results that a statistics engine already computed from NASA data.

Rules you must follow:
1. Use only numbers that appear in [MATERIALS]. Never calculate or invent numbers. If a needed value is missing, say it "was not computed". You may round to about one decimal place.
2. Explain a p-value only as "the probability of seeing a change this large by chance if there were no trend". Never call it "the probability that the trend is real". If it is below 0.001, write "below 0.001".
3. Do not assert causes. Only when documents support it, say "may be related to ..." and put that document id in sources.
4. Do not predict the future. Only compare within the observed period.
5. Do not give orders; frame advice as "things to consider". Never make investment or insurance decisions for the user.
6. If verdict.status is not_significant, say "it is too early to tell" and explain detectable: for need_more give more_years; for length_enough say "the record is already long enough, so the real change may be smaller or none"; for no_trend say "it cannot be estimated".
7. If flags include tests_disagree, state in confidence that the t-test and Mann-Kendall results disagree; if one_year_drives_result, state that removing leave_out_most_extreme.year changes the verdict; if autocorrelation_weakens, state that correcting for autocorrelation weakens significance.
8. In confidence, add one line that results are regional and do not represent a single vineyard. If data_is_mock is true, say it is sample data. If ground_check exists, add one line on the bias versus the nearby weather station.
9. Tailor meaning to user_context.decision. If curious, give only the general meaning.
10. Write in plain English for growers, even if the question is in another language. Gloss technical terms in parentheses. 2–4 sentences per field.

Fields:
- summary: one-line summary — what changed, by how much, and how certain it is.
- numbers: early vs recent averages (early_vs_late), the slope and its 95% confidence interval.
- confidence: verdict, both p-values, the effect of the most extreme year, resolution limits.
- meaning: what it means for a grower — "things to consider" linked to the indicator's how-to-read guide and the decision being weighed.
- next_steps: 2–3 things to check next. change.type is one of threshold (value is one of indicator.threshold_options), region (value is another region id), start_year (a year ≥ indicator.start_year_available), add_variable (value is an indicator id).
- sources: ids of documents you used (documents[].id) and the dataset name.
"""

QUESTION_RULES = """
The user has now asked a free-form question. Keep rules 1–8 and 10 above and answer in 2–6 sentences in the answer field.
If [MATERIALS] cannot answer it, say so and suggest how to check in the tool (change the indicator, region or period).
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
    allowed |= {95.0, 0.05, 5.0, 10.0, 0.001, 0.0001, 0.01}
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
        return "not computed"
    s = f"{x:+.{d}f}"
    return s


def _plain(x: Optional[float], d: int = 1) -> str:
    return "not computed" if x is None else f"{x:.{d}f}"


def _p(x: Optional[float]) -> str:
    if x is None:
        return "not computed"
    return "p < 0.001" if x < 0.001 else f"p = {x:.3f}"


DECISION_TEXT = {
    "variety": "Replanting is a decision that looks decades ahead, so rather than relying on one indicator, consider also checking indicators tied directly to variety suitability, such as GDD, heat days and night temperatures.",
    "frost_invest": "Frost protection pays off by preventing damage in one or two extreme years, so besides the trend direction, consider how often extreme years occurred.",
    "insurance": "In insurance or contract talks this can support 'this trend is observed at the regional level', but it is best to state that it is not evidence of damage in a specific vineyard.",
    "harvest": "When planning harvest dates or labor, consider using the recent 10-year average rather than older long-term norms.",
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
    word = "rose" if v["direction"] == "increase" else "fell" if v["direction"] == "decrease" else "changed"
    tend = "rising" if v["direction"] == "increase" else "falling" if v["direction"] == "decrease" else "flat"

    if v["status"] == "significant":
        summary = (
            f"In {reg['name']}, {ind['name']} {word} by {_n(slope)} {unit} per decade over {per['start']}–{per['end']}, "
            "a change unlikely to be chance (statistically significant)."
        )
    elif v["status"] == "mixed":
        summary = (
            f"In {reg['name']}, {ind['name']} shows a {tend} tendency over {per['start']}–{per['end']}, "
            "but the two tests disagree, so it is too early to call it certain."
        )
    else:
        summary = f"No clear trend in {ind['name']} for {reg['name']} over {per['start']}–{per['end']}. It is too early to tell."

    numbers = (
        f"Early {ev['early']['from']}–{ev['early']['to']} average {_plain(ev['early']['mean'])} {unit} → "
        f"recent {ev['late']['from']}–{ev['late']['to']} average {_plain(ev['late']['mean'])} {unit} (difference {_n(ev['difference'])} {unit}). "
        f"The {tr['method']} is {_n(slope)} {unit} per decade, with a 95% confidence interval (the plausible range of the slope) of {_n(lo)} to {_n(hi)} {unit}."
    )

    conf = [
        f"Verdict: {v['label']}. t-test {_p(tr['p_ttest'])}, Mann-Kendall {_p(tr['p_mann_kendall'])}"
        " (a p-value is the probability of seeing a change this large by chance if there were no trend)."
    ]
    if "tests_disagree" in flags:
        conf.append("The t-test (slope) and Mann-Kendall (rank) results disagree. A few unusually high years may be pulling the slope up.")
    if "one_year_drives_result" in flags:
        conf.append(f"Removing the most extreme year, {lo_ext['year']}, changes the verdict to '{lo_ext['verdict']['label']}'. One year is driving the result.")
    else:
        conf.append(f"Removing the most extreme year, {lo_ext['year']}, leaves the verdict unchanged.")
    if "autocorrelation_weakens" in flags:
        conf.append(f"Correcting for year-to-year persistence (autocorrelation) weakens the t-test to {_p(tr['p_ttest_autocorr_adjusted'])}.")
    if v["status"] != "significant":
        ds = detect_sentence(tr["detectable"])
        conf.append(ds[:1].upper() + ds[1:] + ".")
    conf.append(m["resolution_note"])
    if m.get("ground_check"):
        conf.append(m["ground_check"]["sentence"])
    if m["data_is_mock"]:
        conf.append("This view uses sample data (mock-up).")
    confidence = " ".join(conf)

    bad_up = ind["higher_is"] == "worse"
    bad_down = ind["higher_is"] == "better"
    is_bad = (v["direction"] == "increase" and bad_up) or (v["direction"] == "decrease" and bad_down)
    ext_years = ", ".join(str(e["year"]) for e in m["extremes"])
    if v["status"] == "significant" and is_bad:
        meaning = f"It is moving in a direction that is worse for growers. Memories of extreme years ({ext_years}) may not be just chance."
    elif v["status"] == "significant" and (bad_up or bad_down):
        meaning = f"Risk is moving down, but years with large extremes ({ext_years}) still occurred."
    elif v["status"] == "significant":
        meaning = "The region's climate is steadily shifting. Whether that helps or hurts depends on your varieties and style."
    else:
        meaning = f"Rather than a long-term trend, preparing for year-to-year swings — especially extreme years ({ext_years}) — may be the better lens."
    dec = DECISION_TEXT.get((m.get("user_context") or {}).get("decision") or "curious", "")
    if dec:
        meaning += " " + dec

    steps = []
    opts = [o for o in ind["threshold_options"] if ind["threshold"] is None or float(o) != float(ind["threshold"])]
    if opts:
        steps.append({"label": f"Try a threshold of {opts[-1]}{ind['threshold_unit']}", "change": {"type": "threshold", "value": str(opts[-1])}})
    if m.get("nearest_region"):
        nr = m["nearest_region"]
        steps.append({"label": f"Compare with nearby {nr['name']}", "change": {"type": "region", "value": nr["id"]}})
    rel = RELATED.get(ind["id"])
    if rel and catalog.indicator(rel):
        steps.append({"label": f"Also look at {catalog.indicator(rel)['name']}", "change": {"type": "add_variable", "value": rel}})
    if per["start"] > ind["start_year_available"]:
        steps.append({"label": f"Extend the period to start in {ind['start_year_available']}", "change": {"type": "start_year", "value": str(ind["start_year_available"])}})

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
            "question": "To tailor the insight, which decision are you weighing right now?",
            "options": DECISIONS,
        }

    analysis = run_analysis(req.query)
    m = build_materials(analysis, req.variable_id, {"decision": decision or "curious", "role": req.context.role or "wine grower"})
    payload = "[MATERIALS]\n" + json.dumps(m, ensure_ascii=False)
    sources_allowed = _source_ids(m)

    if req.question:
        try:
            out = llm.structured_call(
                SYSTEM_RULES + QUESTION_RULES,
                [{"role": "user", "content": payload + "\n\n[QUESTION]\n" + req.question}],
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
                "answer": "AI is off, so I can't answer free-form questions. Here is a summary of the computed results instead.\n\n" + card["summary"] + "\n" + card["confidence"],
                "sources": card["sources"],
                "unverified_numbers": [],
                "source": "fallback",
                "fallback_reason": str(e),
            }

    try:
        out = llm.structured_call(
            SYSTEM_RULES,
            [{"role": "user", "content": payload + "\n\nWrite the insight card from the materials above."}],
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
