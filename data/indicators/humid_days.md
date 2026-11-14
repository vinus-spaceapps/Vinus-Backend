---
id: humid_days
name: 생육기 고습일수
category: disease
order: 40
short: 생육기 동안 습도 80% 이상이면서 기온 15~25°C인, 곰팡이병이 번지기 좋은 날 수
unit: 일
dataset: MERRA-2
source: NASA POWER 일별 RH2M·T2M (MERRA-2 2m 상대습도·평균기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
stage_from: budburst
stage_to: harvest
condition: 일평균 상대습도 ≥ 80% 그리고 15°C ≤ 일평균기온 ≤ 25°C
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [습도, 곰팡이, 노균병, 흰가루병, 병해, 방제, 농약, 축축, 습해, disease, humidity]
---

## 정의
생육기 동안 하루 평균 상대습도가 80% 이상이고 하루 평균기온이 15~25°C였던 날의 수입니다. 노균병·흰가루병 같은 곰팡이병이 번지기 좋은 조건입니다.

## 왜 중요한가
곰팡이병은 방제 비용과 수확량 손실의 가장 큰 원인 중 하나입니다. 방제 횟수 계획, 내병성 품종 검토, 유기농 전환 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 병이 번지기 좋은 날이 늘어나는 쪽입니다.
- 건조한 산지(나파·바로사)는 거의 0입니다. 습한 산지(영동·보르도)에서 의미가 큽니다.

## 주의점
- 일평균 습도 기준이라 밤 이슬이나 시간대별 습도는 반영되지 않습니다. 실제 병 발생 모델보다 단순합니다.

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) 2_와인지표_데이터, 7_연도별지표
- NASA POWER — https://power.larc.nasa.gov/
