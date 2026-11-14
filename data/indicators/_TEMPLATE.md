---
# 지표 md 템플릿 — 변수팀이 이 파일을 복사해서 새 지표를 만듭니다.
# 파일 이름은 id 와 같게: data/indicators/<id>.md  (밑줄로 시작하는 파일은 읽지 않습니다)
id: example_indicator            # 영문 소문자·밑줄. 프론트·AI·CSV 경로가 모두 이 값을 씁니다.
name: 예시 지표                   # 카드 제목 (생산자 말로)
category: temp_frost             # temp_frost(기온·서리) | rain_water(비·물) | smoke_air(연기·대기) | growth(생육)
short: 한 줄 정의                 # hover 첫 줄, 변수 담기 AI 가 읽는 정의
unit: 일                          # 그래프 축 단위
dataset: MERRA-2                  # MERRA-2 | GPM IMERG | GLDAS | AIRS | OMI | MODIS
source: MERRA-2 M2SDNXSLV T2MMIN (2m 일 최저기온)
start_year: 1981                  # 해당 데이터로 온전한 첫 시즌
resolution: 약 50km
stage: 발아~개화                  # 집계 기간 (생육 단계)
stage_from: budburst              # budburst | flowering | veraison | harvest | harvest_minus_21
stage_to: flowering
condition: 일 최저기온 < 기준값    # 사람이 읽는 조건
threshold: 0                      # 기준값 (조건이 없으면 비워 둠)
threshold_unit: °C
threshold_options: [0, -1, -2]    # 분석 화면·인사이트 AI 가 바꿔 볼 수 있는 기준값
aggregation: count                # count(날수) | sum(합계) | mean(평균)
robust: false                     # true 면 헤드라인 기울기를 Sen, 튀는 지표(연기 등)에 사용
higher_is: worse                  # worse | better | neutral  (값이 커지면 생산자에게 나쁜가)
keywords: [예시, 키워드]          # 변수 담기 AI 폴백 검색어
---

## 정의
지표를 생산자 말로 2~3문장.

## 왜 중요한가
어떤 결정(품종 교체, 서리 대비 투자, 보험·계약, 수확 계획)에 쓰이는지.

## 해석 가이드
증가/감소가 무엇을 뜻하는지, 기울기를 어떻게 읽는지.

## 주의점
해상도, 결측, 자료 변화점 등.

## 근거
- 출처 제목 — URL
