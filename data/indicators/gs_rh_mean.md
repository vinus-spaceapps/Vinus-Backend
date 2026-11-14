---
id: gs_rh_mean
name: 생육기 평균 습도
category: disease
order: 70
short: 생육기 동안 하루 평균 상대습도의 평균
unit: "%"
dataset: MERRA-2
source: NASA POWER 일별 RH2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
keywords: [습도, 눅눅, 병해, 곰팡이, 방제]
---

## 정의
생육기 동안 하루 평균 상대습도를 평균한 값입니다.

## 왜 중요한가
습한 산지일수록 곰팡이병 방제 비용이 큽니다. 습도가 오르는지 내리는지로 방제 계획과 내병성 품종 판단을 합니다.

## 해석 가이드
- 기울기가 양수면 생육기가 눅눅해지는 쪽입니다.

## 주의점
- 하루 평균값으로 계산한 근사입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
