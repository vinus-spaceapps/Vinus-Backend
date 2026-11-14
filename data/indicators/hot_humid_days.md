---
id: hot_humid_days
name: 덥고 습한 날
category: disease
order: 50
short: 생육기 동안 평균기온 25°C 이상이면서 습도 70% 이상인 무더운 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 T2M·RH2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: 일 평균기온 ≥ 25°C 그리고 상대습도 ≥ 70%
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [무더위, 덥고 습한, 탄저병, 신부패, 장마]
---

## 정의
생육기 동안 하루 평균기온이 25°C 이상이고 상대습도가 70% 이상이었던 날의 수입니다.

## 왜 중요한가
덥고 습하면 신부패병·탄저병 같은 고온성 병이 번지고 포도알이 쉽게 상합니다. 영동처럼 장마철이 더운 산지의 방제 계획에 씁니다.

## 해석 가이드
- 기울기가 양수면 무더운 날이 늘어나는 쪽입니다.

## 주의점
- 하루 평균값으로 계산한 근사입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
