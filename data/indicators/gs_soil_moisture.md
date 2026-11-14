---
id: gs_soil_moisture
name: 생육기 뿌리층 토양수분
category: drought
order: 100
short: 생육기 동안 뿌리가 있는 깊이의 흙이 얼마나 젖어 있는지(0=마름, 1=흠뻑)의 평균
unit: 0~1
dataset: MERRA-2
source: NASA POWER 일별 GWETROOT (MERRA-2 뿌리층 토양 습윤도)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
stage_from: budburst
stage_to: harvest
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: better
keywords: [가뭄, 건조, 토양, 흙, 수분, 물 부족, 관수, 관개, 물주기, 메마른, drought, soil]
---

## 정의
생육기 동안 뿌리가 뻗는 깊이(뿌리층)의 흙이 얼마나 젖어 있는지를 0(완전히 마름)부터 1(물로 가득 참) 사이 값으로 나타내 평균한 것입니다.

## 왜 중요한가
포도나무는 적당한 물 스트레스에서 좋은 포도를 맺지만, 너무 마르면 잎이 지고 당 축적이 멈춥니다. 관수 시설 투자, 대목(뿌리) 교체, 내건성 품종 검토에 씁니다.

## 해석 가이드
- 기울기가 음수면 생육기 흙이 점점 마르는 쪽입니다.
- 비가 늘어도 기온이 올라 증발이 늘면 토양수분은 줄 수 있습니다.

## 주의점
- 모델 값이며, 관수한 밭의 실제 토양수분과 다릅니다.
- GLDAS Noah 2.1(약 25km)로 교차 확인할 계획입니다.

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) 7_연도별지표
- NASA POWER — https://power.larc.nasa.gov/
