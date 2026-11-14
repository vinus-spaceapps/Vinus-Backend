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
  regions.json       산지 7곳
  series/            실제 NASA 집계값 CSV 넣는 곳 (README 참고)
tests/               통계 검증(scipy 대조) + 기획서 5가지 판정 케이스 + API 흐름
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

## 예시 데이터와 실제 데이터

지금 분석 결과는 `app/series.py`가 만드는 **예시 데이터(목업)**이고 화면에 배지가 붙습니다. 실제 NASA 집계값을 `data/series/<변수id>/<산지id>.csv`에 넣으면 그 조합은 자동으로 실제 값으로 바뀝니다. 형식은 [data/series/README.md](data/series/README.md)를 보세요.

## AI 설정

| 환경변수 | 설명 |
|---|---|
| `ANTHROPIC_API_KEY` | 없으면 AI 폴백 |
| `VINUS_LLM_MODEL` | 기본 `claude-opus-5-5` |
| `VINUS_AI_DISABLED=1` | 키가 있어도 AI 끄기 (시연 리허설용) |
| `VINUS_LLM_NO_SERVER_FALLBACK=1` | 거절 시 서버 측 대체 모델(`fallbacks="default"`) 끄기 |
