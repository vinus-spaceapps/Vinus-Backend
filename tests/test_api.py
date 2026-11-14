"""API 흐름 테스트. AI 는 꺼진 상태(폴백)로 전체 흐름이 도는지 확인합니다."""

import os

os.environ["VINUS_AI_DISABLED"] = "1"

from fastapi.testclient import TestClient  # noqa: E402

from app.ai.insight_agent import unverified_numbers  # noqa: E402
from app.main import app  # noqa: E402

client = TestClient(app)
QUERY = {"variables": ["harvest_smoke_days"], "region": "rogue_valley", "start": 2003, "end": 2025}


def test_health_reports_ai_off():
    r = client.get("/api/health").json()
    assert r["ok"] is True
    assert r["ai"]["enabled"] is False


def test_variables_have_hover_content():
    data = client.get("/api/variables").json()
    assert len(data["categories"]) == 4
    assert len(data["variables"]) >= 6
    for v in data["variables"]:
        assert v["short"] and v["unit"] and v["dataset"]
        assert v["sections"]["definition"] and v["sections"]["why"]
    datasets = {v["dataset"] for v in data["variables"]}
    assert {"MERRA-2", "GPM IMERG", "GLDAS", "AIRS", "OMI", "MODIS"} <= datasets


def test_analyze_main_demo():
    r = client.post("/api/analyze", json=QUERY)
    assert r.status_code == 200
    res = r.json()["results"][0]
    assert res["stats"]["verdict"]["label"] == "증가, 유의함"
    assert res["is_mock"] is True
    assert len(res["series"]) == 23
    assert len(res["regions"]) == 7
    assert all("q_mk" in c for c in res["regions"])
    assert "로그 밸리 · 수확기 연기 노출일수 · 2003~2025" in res["verdict_text"]


def test_analyze_clamps_to_dataset_start():
    r = client.post("/api/analyze", json={**QUERY, "variables": ["harvest_aerosol_days"], "start": 1990}).json()
    res = r["results"][0]
    assert res["start"] == 2005
    assert any("2005" in n for n in res["notes"])


def test_threshold_change_reduces_counts():
    base = client.post("/api/analyze", json={**QUERY, "variables": ["frost_after_budburst"], "region": "mosel"}).json()
    strict = client.post(
        "/api/analyze",
        json={**QUERY, "variables": ["frost_after_budburst"], "region": "mosel", "thresholds": {"frost_after_budburst": -2}},
    ).json()
    s0 = sum(p["value"] for p in base["results"][0]["series"])
    s1 = sum(p["value"] for p in strict["results"][0]["series"])
    assert s1 < s0


def test_user_overlay_correlation():
    pts = [{"year": y, "value": float(y % 7)} for y in range(2005, 2025)]
    r = client.post("/api/analyze", json={**QUERY, "user_series": pts, "user_label": "수확량"}).json()
    ov = r["results"][0]["overlay"]
    assert ov["common_years"] == 20
    assert ov["correlation"] is not None


def test_bad_requests():
    assert client.post("/api/analyze", json={**QUERY, "region": "mars"}).status_code == 400
    assert client.post("/api/analyze", json={**QUERY, "variables": ["nope"]}).status_code == 400
    assert client.post("/api/analyze", json={**QUERY, "variables": []}).status_code == 422


def test_variable_ai_fallback_adds_frost():
    r = client.post("/api/ai/variables", json={"messages": [{"role": "user", "content": "봄마다 서리 때문에 걱정이야"}], "basket": []}).json()
    assert r["source"] == "fallback"
    assert "frost_after_budburst" in [a["id"] for a in r["add"]]
    assert len(r["add"]) <= 3


def test_variable_ai_fallback_asks_when_vague():
    r = client.post("/api/ai/variables", json={"messages": [{"role": "user", "content": "요즘 좀 걱정이네"}], "basket": []}).json()
    assert r["add"] == []
    assert "?" in r["reply"]


def test_variable_ai_fallback_explains():
    r = client.post("/api/ai/variables", json={"messages": [{"role": "user", "content": "적산온도가 뭐야?"}], "basket": []}).json()
    assert r["add"] == []
    assert "적산온도" in r["reply"]


def test_variable_ai_respects_basket_limit():
    full = ["heat_days", "gdd_growing_season", "harvest_rain_days"]
    r = client.post("/api/ai/variables", json={"messages": [{"role": "user", "content": "서리 걱정"}], "basket": full}).json()
    assert r["add"] == []


def test_insight_asks_decision_first():
    r = client.post("/api/ai/insight", json={"query": QUERY, "variable_id": "harvest_smoke_days"}).json()
    assert r["type"] == "need_context"
    assert len(r["options"]) == 5


def test_insight_fallback_card_has_six_parts():
    r = client.post(
        "/api/ai/insight", json={"query": QUERY, "variable_id": "harvest_smoke_days", "context": {"decision": "insurance"}}
    ).json()
    assert r["type"] == "card"
    card = r["card"]
    for k in ("summary", "numbers", "confidence", "meaning", "next_steps", "sources"):
        assert card[k]
    assert "산지 단위" in card["confidence"]
    assert "추세가 없을 때" in card["confidence"]
    assert 1 <= len(card["next_steps"]) <= 3


def test_insight_fallback_mentions_disagreement_and_detectable():
    q = {**QUERY, "variables": ["frost_after_budburst"], "region": "barossa"}
    r = client.post("/api/ai/insight", json={"query": q, "variable_id": "frost_after_budburst", "context": {"decision": "frost_invest"}}).json()
    assert "엇갈" in r["card"]["confidence"]


def test_insight_fallback_mentions_one_year():
    q = {**QUERY, "variables": ["harvest_rain_days"], "region": "yeongdong"}
    r = client.post("/api/ai/insight", json={"query": q, "variable_id": "harvest_rain_days", "context": {"decision": "harvest"}}).json()
    assert "빼면 판정이" in r["card"]["confidence"]


def test_unverified_number_guard():
    materials = {"trend": {"slope_per_decade": 4.0, "p": 0.0012}, "period": {"start": 2003, "end": 2025}}
    assert unverified_numbers(["10년에 4.0일 늘었고 2003~2025"], materials) == []
    assert unverified_numbers(["10년에 37.5일 늘었습니다"], materials) == ["37.5"]
