---
id: heat_degree_sum
name: 고온 누적
category: heat
order: 30
short: 생육기 동안 최고기온이 기준값(기본 35°C)을 넘은 만큼을 모두 더한 값. 더위 피해의 총량
unit: "°C·일"
dataset: MERRA-2
source: NASA POWER 일별 T2M_MAX
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: Σ max(0, 일 최고기온 − 기준값)
threshold: 35
threshold_unit: °C
threshold_options: [32, 35]
aggregation: sum
robust: false
higher_is: worse
station_var: tmax
keywords: [고온 누적, 열 스트레스, 폭염 강도, 더위 피해]
---

## 정의
생육기 중 매일 최고기온이 기준값(기본 35°C)을 넘은 만큼(예: 38°C면 3)을 모두 더한 값입니다. 32°C로 바꿔 볼 수 있습니다.

## 왜 중요한가
폭염일수가 '며칠'이라면 이것은 '얼마나 세게'입니다. 40°C 하루가 36°C 하루보다 훨씬 큰 피해를 주는 것을 반영해, 폭염 대비 투자 규모를 가늠하는 데 씁니다.

## 해석 가이드
- 기울기가 양수면 더위 피해의 총량이 커지는 쪽입니다.

## 주의점
- 50km 격자 평균이라 고도·경사면 차이는 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
