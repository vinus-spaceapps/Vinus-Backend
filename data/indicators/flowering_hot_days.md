---
id: flowering_hot_days
name: 개화기 고온일수
category: heat
order: 90
short: 꽃이 피는 달(6월) 동안 최고기온이 기준값(기본 32°C) 이상인 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 T2M_MAX
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 개화기 (6월, 남반구 12월)
condition: 일 최고기온 ≥ 기준값
threshold: 32
threshold_unit: °C
threshold_options: [30, 32, 35]
aggregation: count
robust: false
higher_is: worse
station_var: tmax
keywords: [개화, 꽃, 착과, 고온, 꽃가루]
---

## 정의
개화기 동안 하루 최고기온이 기준값(기본 32°C) 이상이었던 날의 수입니다. 30·35°C로 바꿔 볼 수 있습니다.

## 왜 중요한가
꽃이 필 때 너무 더우면 꽃가루가 힘을 잃어 열매가 덜 맺힙니다. 개화기 저온일수와 함께 그해 착과(수확량)를 가늠하는 데 씁니다.

## 해석 가이드
- 기울기가 양수면 개화기 더위가 늘어나는 쪽입니다.

## 주의점
- 실제 개화 시기는 해마다·품종마다 달라 한 달 고정 기간은 근사입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
