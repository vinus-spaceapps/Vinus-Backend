---
id: harvest_warm_nights
name: 수확기 따뜻한 밤
category: heat
order: 80
short: 수확기(8~9월) 동안 밤 최저기온이 기준값(기본 15°C) 이상으로 덥던 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 T2M_MIN
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 수확기 (8~9월, 남반구 2~3월)
condition: 일 최저기온 ≥ 기준값
threshold: 15
threshold_unit: °C
threshold_options: [12, 15, 18]
aggregation: count
robust: false
higher_is: worse
station_var: tmin
keywords: [따뜻한 밤, 열대야, 수확기 밤, 산도, 색]
---

## 정의
수확기 동안 하루 최저기온이 기준값(기본 15°C) 이상이었던 날의 수입니다. 12·18°C로 바꿔 볼 수 있습니다.

## 왜 중요한가
익는 시기 밤이 따뜻하면 포도가 밤새 호흡으로 산을 소모하고 색이 덜 듭니다. 서늘한 밤 지수(9월 평균)보다 '며칠이나'를 직접 보여 줍니다.

## 해석 가이드
- 기울기가 양수면 익는 시기 따뜻한 밤이 늘어나는 쪽입니다.

## 주의점
- 50km 격자 평균이라 고도·경사면 차이는 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
