"""API 흐름 테스트. AI 는 꺼진 상태(폴백)로 전체 흐름이 도는지 확인합니다."""

import os

os.environ["VINUS_AI_DISABLED"] = "1"

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from app import analysis  # noqa: E402
from app.ai.insight_agent import unverified_numbers  # noqa: E402
from app.main import app  # noqa: E402
from app.series import SeriesResult  # noqa: E402

client = TestClient(app)
QUERY = {"variables": ["gdd_growing_season"], "region": "yeongdong", "start": 2001, "end": 2026}
SMOKE = {"variables": ["harvest_smoke_days"], "region": "napa", "start": 2003, "end": 2026}


def test_health_reports_ai_off():
    r = client.get("/api/health").json()
    assert r["ok"] is True
    assert r["ai"]["enabled"] is False


def test_variables_have_hover_content():
    data = client.get("/api/variables").json()
    assert len(data["categories"]) == 8
    core = [v for v in data["variables"] if v["family"] == "core"]
    assert len(core) == 100
    assert len(data["variables"]) >= 900
    assert {f["id"] for f in data["families"]} == {"core", "etccdi", "extremes", "stats"}
    cats = {c["id"] for c in data["categories"]}
    assert all(v["category"] in cats for v in data["variables"])
    for v in data["variables"]:
        assert v["short"] and v["unit"] and v["dataset"]
        assert v["sections"]["definition"] and v["sections"]["why"]
    datasets = {v["dataset"] for v in data["variables"]}
    assert {"MERRA-2", "MODIS"} <= datasets


def test_regions_match_team_data():
    ids = {r["id"] for r in client.get("/api/regions").json()}
    assert ids == {"burgundy", "bordeaux", "mosel", "okanagan", "napa", "barossa", "yeongdong"}


def test_analyze_real_data():
    r = client.post("/api/analyze", json=QUERY)
    assert r.status_code == 200
    body = r.json()
    res = body["results"][0]
    assert res["is_mock"] is False
    assert body["is_mock"] is False
    assert len(res["series"]) == 26
    assert res["stats"]["verdict"]["label"] == "증가, 유의함"
    assert len(res["regions"]) == 7
    assert all("q_mk" in c for c in res["regions"])
    assert "충북 영동 · 생육기 적산온도 · 2001~2026" in res["verdict_text"]


def test_analyze_mock_indicator_is_flagged():
    res = client.post("/api/analyze", json=SMOKE).json()["results"][0]
    assert res["is_mock"] is True
    assert "예시" in res["source_note"]


def test_analyze_reports_missing_years():
    res = client.post("/api/analyze", json={**QUERY, "variables": ["greenup_doy"]}).json()["results"][0]
    assert res["end"] == 2025
    assert any("2026" in n for n in res["notes"])


def test_analyze_clamps_to_dataset_start():
    r = client.post("/api/analyze", json={**QUERY, "variables": ["winter_min_temp"], "start": 1990}).json()
    res = r["results"][0]
    assert res["start"] == 2002
    assert any("2002" in n for n in res["notes"])


def test_threshold_variant_uses_real_file():
    base = client.post("/api/analyze", json={**QUERY, "variables": ["heat_days"]}).json()["results"][0]
    hot = client.post("/api/analyze", json={**QUERY, "variables": ["heat_days"], "thresholds": {"heat_days": 30}}).json()["results"][0]
    assert hot["is_mock"] is False
    assert hot["threshold"] == 30
    assert sum(p["value"] for p in hot["series"]) > sum(p["value"] for p in base["series"])


def test_unknown_threshold_is_refused_not_invented():
    r = client.post("/api/analyze", json={**QUERY, "variables": ["heat_days"], "thresholds": {"heat_days": 33}})
    assert r.status_code == 400
    assert "실제 집계가 아직 없습니다" in r.json()["detail"]


def test_daily_derived_indicators_are_real():
    data = client.get("/api/variables").json()["variables"]
    real = [v for v in data if v["has_real_data"]]
    assert len(real) >= 25
    for vid in ("gst_mean", "tropical_nights", "dry_spell_max", "frost_free_days"):
        res = client.post("/api/analyze", json={**QUERY, "variables": [vid]}).json()["results"][0]
        assert res["is_mock"] is False, vid
    hot = client.post("/api/analyze", json={**QUERY, "variables": ["heat_days"], "thresholds": {"heat_days": 32}}).json()["results"][0]
    assert hot["is_mock"] is False


def test_generated_families_analyze():
    for vid in ("m_04_tmin_min", "s_summer_vpd_max", "x_gs_tn90", "etccdi_su", "etccdi_gsl"):
        r = client.post("/api/analyze", json={**QUERY, "variables": [vid]})
        assert r.status_code == 200, (vid, r.text)
        res = r.json()["results"][0]
        assert res["is_mock"] is False
        assert len(res["series"]) >= 20
        assert len(res["regions"]) == 7


def test_variable_ai_keeps_to_core_indicators():
    r = client.post("/api/ai/variables", json={"messages": [{"role": "user", "content": "4월 최저기온 서리"}], "basket": []}).json()
    assert r["add"] and r["add"][0]["id"] == "frost_after_budburst"


def test_no_frost_region_explains_instead_of_inventing():
    r = client.post("/api/analyze", json={**QUERY, "variables": ["last_spring_frost"], "region": "barossa", "thresholds": {"last_spring_frost": -2}})
    assert r.status_code == 400
    assert "연도가 0개" in r.json()["detail"]


def test_validation_attached():
    body = client.post("/api/analyze", json={**QUERY, "region": "mosel"}).json()
    assert body["validation"]["station"]["id"]


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
    r = client.post("/api/ai/insight", json={"query": QUERY, "variable_id": "gdd_growing_season"}).json()
    assert r["type"] == "need_context"
    assert len(r["options"]) == 5


def test_insight_fallback_card_has_six_parts():
    r = client.post("/api/ai/insight", json={"query": QUERY, "variable_id": "gdd_growing_season", "context": {"decision": "variety"}}).json()
    assert r["type"] == "card"
    card = r["card"]
    for k in ("summary", "numbers", "confidence", "meaning", "next_steps", "sources"):
        assert card[k]
    assert "산지 단위" in card["confidence"]
    assert "추세가 없을 때" in card["confidence"]
    assert "예시 데이터" not in card["confidence"]
    assert 1 <= len(card["next_steps"]) <= 3


def test_insight_fallback_mentions_station_check():
    q = {**QUERY, "variables": ["frost_after_budburst"], "region": "okanagan"}
    r = client.post("/api/ai/insight", json={"query": q, "variable_id": "frost_after_budburst", "context": {"decision": "frost_invest"}}).json()
    assert "관측소" in r["card"]["confidence"]
    assert "변화 방향" in r["card"]["confidence"]  # 오카나간은 오차가 커서 경고


@pytest.fixture
def spiky_series(monkeypatch):
    """두 검정이 엇갈리고, 가장 튄 해를 빼면 판정이 바뀌는 합성 시계열."""
    years = list(range(2003, 2026))
    values = [3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 12, 3, 14]

    def fake(meta, region_id, start, end, threshold=None):
        return SeriesResult(years, [float(v) for v in values], False, "테스트용 합성 시계열")

    monkeypatch.setattr(analysis, "get_series", fake)


def test_insight_fallback_mentions_disagreement_and_one_year(spiky_series):
    q = {**QUERY, "variables": ["harvest_rain_days"], "region": "yeongdong"}
    r = client.post("/api/ai/insight", json={"query": q, "variable_id": "harvest_rain_days", "context": {"decision": "harvest"}}).json()
    conf = r["card"]["confidence"]
    assert "엇갈" in conf
    assert "빼면 판정이" in conf


def test_unverified_number_guard():
    materials = {"trend": {"slope_per_decade": 4.0, "p": 0.0012}, "period": {"start": 2003, "end": 2025}}
    assert unverified_numbers(["10년에 4.0일 늘었고 2003~2025"], materials) == []
    assert unverified_numbers(["10년에 37.5일 늘었습니다"], materials) == ["37.5"]
