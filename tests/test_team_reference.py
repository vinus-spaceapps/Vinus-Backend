"""엔진 결과가 팀 참고 계산(엑셀 6_추세검정결과)과 같은지 확인합니다.

기준값은 scripts/import_team_xlsx.py 가 tests/fixtures/team_trend_results.csv 로 내보냅니다.
엑셀 값은 기울기 소수 셋째 자리, p값 넷째 자리로 반올림되어 있어 그만큼의 차이는 허용합니다.
"""

import csv
from pathlib import Path

import pytest

from app.stats import mann_kendall, ols_trend, sen_slope

ROOT = Path(__file__).resolve().parent.parent
FIXTURE = ROOT / "tests" / "fixtures" / "team_trend_results.csv"
SERIES = ROOT / "data" / "series"

ROWS = list(csv.DictReader(FIXTURE.open(encoding="utf-8"))) if FIXTURE.exists() else []


def _load(row):
    name = f"{row['region']}.csv" if not row["threshold"] else f"{row['region']}__t{float(row['threshold']):g}.csv"
    data = {int(r["year"]): float(r["value"]) for r in csv.DictReader((SERIES / row["variable"] / name).open(encoding="utf-8"))}
    years = [y for y in range(int(row["start"]), int(row["end"]) + 1) if y in data]
    return years, [data[y] for y in years]


@pytest.mark.skipif(not ROWS, reason="팀 기준값 파일이 없습니다")
@pytest.mark.parametrize("row", ROWS, ids=lambda r: f"{r['region']}-{r['variable']}-{r['threshold'] or 'def'}")
def test_matches_team_reference(row):
    years, values = _load(row)
    assert len(years) == int(row["n"])
    ols = ols_trend(years, values)
    assert ols["slope"] * 10 == pytest.approx(float(row["ols_per_decade"]), abs=1e-3)
    assert ols["ci_low"] * 10 == pytest.approx(float(row["ols_ci_low"]), abs=1e-3)
    assert ols["ci_high"] * 10 == pytest.approx(float(row["ols_ci_high"]), abs=1e-3)
    assert ols["p"] == pytest.approx(float(row["t_p"]), abs=2e-4)
    assert sen_slope(years, values)["slope"] * 10 == pytest.approx(float(row["sen_per_decade"]), abs=1e-3)
    if row["mk_p"]:  # 값이 모두 같은 지표는 팀 표에서 비어 있음
        assert mann_kendall(values)["p"] == pytest.approx(float(row["mk_p"]), abs=2e-4)
