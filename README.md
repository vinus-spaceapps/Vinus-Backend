# Vinus-Backend

와인 기후 추세 탐정 API — NASA Space Apps Challenge 2026 (Be An Earth System Trend Detective!)

숫자는 이 서버의 통계 엔진만 계산합니다. AI(변수 담기·인사이트)는 엔진 결과를 고르고 설명만 하고, 키가 없거나 꺼져도 규칙 기반 폴백으로 전체 흐름이 돕니다.

## 실행

Python 3.10 이상을 권장합니다 (CI는 3.12). 3.9에서도 돌지만 Claude SDK가 설치되지 않아 AI는 폴백으로만 동작합니다.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt -r requirements-dev.txt
cp .env.example .env        # AI를 쓰려면 ANTHROPIC_API_KEY 입력
.venv/bin/uvicorn app.main:app --reload --port 8000
```

- API 문서: http://localhost:8000/docs
- 테스트: `.venv/bin/python -m pytest -q`
- CI와 같은 lint: `.venv/bin/ruff check --select E9,F63,F7,F82,F401 .`

## API

| 메서드 | 경로 | 하는 일 |
|---|---|---|
| GET | `/api/health` | 서버·AI 상태 |
| GET | `/api/variables` | 카테고리 + 변수 목록 (hover 소개 문구 포함) |
| GET | `/api/regions` | 산지 목록 (좌표, 생육 단계 기본 날짜) |
| POST | `/api/analyze` | 시계열 + 변화율 + 유의성 + 판정 + 다른 산지 비교 |
| POST | `/api/ai/variables` | 변수 담기 AI → `{reply, add:[{id, reason}]}` |
| GET | `/api/ai/decisions` | 인사이트 AI가 묻는 결정 맥락 목록 |
| POST | `/api/ai/insight` | 인사이트 AI → 결정 맥락 질문, 6칸 카드, 또는 자유 질문 답변 |

`/api/analyze` 요청 예:

```json
{"variables": ["harvest_smoke_days"], "region": "rogue_valley", "start": 2003, "end": 2025,
 "thresholds": {"harvest_smoke_days": 2.0}, "user_series": [{"year": 2015, "value": 3.2}]}
```

## 구조

```
app/
  main.py            FastAPI 라우트
  stats.py           통계 엔진 (OLS·Sen·Mann-Kendall·신뢰구간·탐지 가능 연수·FDR·자기상관 보정)
  analysis.py        요청 → 결과 묶음, 인사이트 AI 재료(build_materials)
  series.py          연도별 시계열 공급 (실제 CSV 우선, 없으면 예시 데이터)
  catalog.py         지표 md·산지 목록 로더
  ai/llm.py          Claude 호출 (구조화 출력, 거절 시 서버 측 대체 모델)
  ai/variable_agent.py  변수 담기 AI + 키워드 폴백
  ai/insight_agent.py   인사이트 AI + 템플릿 폴백 + 숫자 검증
data/
  indicators/*.md    지표 md (변수팀이 편집, _TEMPLATE.md 참고)
  regions.json       산지 7곳 (팀 3_산지좌표 기준)
  series/            연도별 실제 집계값 CSV (README 참고)
  validation.json    지상 관측소·MODIS 1km 비교 요약
scripts/
  import_team_xlsx.py  팀 엑셀 → series·validation·대조 기준
tests/               scipy 대조 + 팀 참고 계산 대조(84건) + 기획서 5가지 판정 케이스 + API 흐름
```

## 판정 규칙

| 상태 | 조건 | 화면 문구 |
|---|---|---|
| significant | t-검정과 Mann-Kendall 모두 p < 0.05 | 증가, 유의함 / 감소, 유의함 |
| mixed | 둘 중 하나만 p < 0.05 | 증가 경향, 검정 결과 엇갈림 |
| not_significant | 둘 다 p ≥ 0.05 | 유의하지 않음 + 탐지 가능 연수 |

- 헤드라인 기울기: 지표 md의 `robust: true`(연기 등 튀는 지표)면 Sen, 아니면 OLS. 단위는 10년당.
- 함께 계산하는 것: 가장 튄 해를 뺀 재검정, 초기 10년 vs 최근 10년 평균, 극단값 상위 3개 연도, 잔차 자기상관 보정 p값, 다른 산지 비교의 FDR q값.
- 탐지 가능 연수는 Weatherhead et al. (1998) 근사식입니다.

## 데이터

**실제 값**: 산지 7곳 × 2001~2026년, 지표 100개 중 98개. 모두 팀 엑셀(`NASA_와인_데이터정리.xlsx`)에서 나왔습니다. 카테고리 8개(기온·서리 17, 더위 9, 비 19, 가뭄·토양 14, 병해·습도 8, 햇빛·바람 8, 연기·대기 2, 생육·시기 23).

| 출처 | 지표 수 | 내용 |
|---|---|---|
| 팀이 계산한 연도별 값 (`7_연도별지표`, `8`, `15`) | 15 | 서리일수, 겨울 최저기온, 폭염일수, 적산온도, Huglin, 서늘한 밤 지수, 수확기 강수·호우, 고습일수, 토양수분, 그린업, 봄 밤 지표면 온도, 1km 냉기 구간 |
| 일별 원자료(`D_*`, NASA POWER = MERRA-2·CERES)로 직접 계산 | 83 | 생육 단계(겨울·봄·개화기·여름·수확기·가을)별 기온·강수·습도·토양수분·일사·바람, 병해 위험일(노균병·흰가루병·잿빛곰팡이), 물수지·VPD, 서리·한파·폭염의 횟수·세기·지속, 생육 시작·종료·적산온도 도달일 등 (`scripts/import_team_xlsx.py`의 `DERIVED`) |

**자동 생성 지표 849개** (`scripts/generate_families.py`, 결과는 `data/series_generated/<산지>.csv` + `data/indicators_generated.json`):

| 묶음 | 개수 | 만드는 방식 |
|---|---|---|
| 월·계절 기본 통계 (`m_*`, `s_*`) | 722 | 변수 13개 × 기간 20개(1~12월, 겨울·봄·여름·가을, 생육기·수확기·휴면기·시즌 1년) × 평균·최솟값·최댓값 (강수: 합계·최댓값·비 온 날수). 핵심 지표와 같은 조합은 뺌 |
| 평년 대비 극값 일수 (`x_*`) | 100 | 기간 20개 × 평년(2001~2010) 상위 10% 더운 낮·따뜻한 밤, 하위 10% 서늘한 낮·추운 밤, 상위 5% 큰비 |
| 기후 극값 지수 ETCCDI (`etccdi_*`) | 27 | WMO 표준 지수 (FD, SU, ID, TR, GSL, TXx, TNx, TXn, TNn, TN10p, TX10p, TN90p, TX90p, WSDI, CSDI, DTR, Rx1day, Rx5day, SDII, R10mm, R20mm, R50mm, CDD, CWD, R95p, R99p, PRCPTOT) |

남반구는 같은 생육 단계끼리 비교되도록 달을 6개월 밀어 맞춥니다. 변수 담기 AI 에게는 핵심 지표 100개만 보여 줍니다.

**지표가 많을수록 우연히 유의하게 나오는 것도 늘어납니다** (2001~2026, t-검정·Mann-Kendall 둘 다 p<0.05 를 '유의'로):

| 범위 | 검정 수 | 유의 | 우연 기대 | 전체 FDR(BH) q<0.05 |
|---|---|---|---|---|
| 핵심 100 | 698 | 151 | 약 35 | 4 (영동 적산온도·그린업·생육기 평균기온·Huglin) |
| ETCCDI 27 | 189 | 40 | 약 9 | 10 |
| 전체 949 | 6,637 | 990 | 약 332 | 0 (q<0.1 은 29) |

발표에서 "몇 개가 유의했다"고 말할 때는 묶음 단위로 보정한 숫자를 쓰는 것이 안전합니다. 지금 화면의 FDR 보정은 같은 지표의 산지 7곳 사이에만 적용합니다.

일별 계산은 먼저 팀 지표 9개를 같은 원자료로 다시 계산해 팀 값과 모두 일치하는지 확인한 뒤(스크립트가 실행할 때마다 출력), 같은 기간·방식으로 만듭니다. 지표를 결과의 유의성으로 고르지 않았습니다.

**예시 데이터(목업)**: 연기 지표 2개(AIRS 일산화탄소, OMI 에어로졸)만 아직 실제 집계가 없어 `app/series.py`가 만든 값을 쓰고, 응답에 `is_mock: true`, 화면에 배지가 붙습니다. 실제 집계가 있는 지표는 없는 기준값·산지를 지어내지 않고 400으로 알립니다.

**엑셀이 바뀌면** 아래 한 줄로 `data/series/*.csv`, `data/validation.json`(관측소·MODIS 검증), `tests/fixtures/team_trend_results.csv`(엔진 대조 기준)를 다시 만듭니다. 엑셀 파일 자체는 커밋하지 않습니다.

```bash
.venv/bin/python scripts/import_team_xlsx.py ~/Downloads/NASA_와인_데이터정리.xlsx
```

- 엔진 대조: `tests/test_team_reference.py`가 팀 참고 계산(엑셀 `6_추세검정결과` 84행)과 OLS·신뢰구간·t-검정·Sen·Mann-Kendall이 반올림 범위 안에서 같은지 확인합니다.
- CSV 형식과 파일 이름 규칙: [data/series/README.md](data/series/README.md)

## AI 설정

| 환경변수 | 설명 |
|---|---|
| `VINUS_LLM_PROVIDER` | `openai` 또는 `anthropic`. 비우면 `OPENAI_API_KEY`가 있을 때 openai |
| `OPENAI_API_KEY` | OpenAI 키 (Python 3.9에서도 동작) |
| `VINUS_OPENAI_MODEL` | 기본 `gpt-5.4-mini` |
| `ANTHROPIC_API_KEY` | Claude 키 (Python 3.10+). 둘 다 없으면 AI 폴백 |
| `VINUS_LLM_MODEL` | Claude 모델, 기본 `claude-opus-5-5` |
| `VINUS_AI_DISABLED=1` | 키가 있어도 AI 끄기 (시연 리허설용) |
| `VINUS_LLM_NO_SERVER_FALLBACK=1` | 거절 시 서버 측 대체 모델(`fallbacks="default"`) 끄기 |

## 실서버 (Railway)

| 항목 | 값 |
|---|---|
| 주소 | https://vinus-backend-production.up.railway.app (API 문서 `/docs`) |
| Railway | 프로젝트 `vinus`, 서비스 `vinus-backend` |
| 실행 | `Procfile` (uvicorn, `0.0.0.0`, Railway 가 주는 `PORT`) |
| Python | `.python-version` = 3.12 (CI 와 같음) |

서비스 설정값(Railway 대시보드 또는 `railway variable`):

| 이름 | 값 |
|---|---|
| `OPENAI_API_KEY` | OpenAI 키 (값은 저장소에 두지 않음) |
| `VINUS_LLM_PROVIDER` | `openai` |
| `VINUS_OPENAI_MODEL` | `gpt-5.4-mini` |
| `VINUS_CORS_ORIGINS` | 프론트 주소 (쉼표로 여러 개, 예: `https://vinus-frontend-production.up.railway.app,http://localhost:5173`) |

지금은 GitHub 와 연결하지 않고 로컬 폴더에서 바로 올립니다. push 해도 자동으로 다시 배포되지 않으니, 코드를 바꾸면 이 폴더에서 다시 올리세요.

```bash
npm install -g @railway/cli   # 처음 한 번
railway login                 # 처음 한 번
railway link --project vinus  # 처음 한 번, 서비스는 vinus-backend
railway up --service vinus-backend
```

`.env`·`.venv` 는 `.gitignore` 에 있어 올라가지 않습니다.
