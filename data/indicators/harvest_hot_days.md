---
id: harvest_hot_days
name: 수확기 고온일수
category: heat
order: 70
short: 수확기(8~9월) 동안 최고기온이 기준값(기본 30°C) 이상인 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 T2M_MAX
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 수확기 (8~9월, 남반구 2~3월)
condition: 일 최고기온 ≥ 기준값
threshold: 30
threshold_unit: °C
threshold_options: [30, 32, 35]
aggregation: count
robust: false
higher_is: worse
station_var: tmax
keywords: [수확기 더위, 숙성기 고온, 산도, 향, 알코올]
---

## 정의
수확기 동안 하루 최고기온이 기준값(기본 30°C) 이상이었던 날의 수입니다. 32·35°C로 바꿔 볼 수 있습니다.

## 왜 중요한가
익는 시기의 더위는 산도와 향을 빠르게 빼앗고 당만 올려, 알코올이 높고 밋밋한 와인이 됩니다. 수확 시기를 앞당길지, 그늘을 늘릴지 판단할 때 씁니다.

## 해석 가이드
- 기울기가 양수면 익는 시기에 더운 날이 늘어나는 쪽입니다.

## 주의점
- 50km 격자 평균이라 고도·경사면 차이는 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
