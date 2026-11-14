---
id: harvest_tmin_mean
name: 수확기 평균 최저기온
category: growth
order: 140
short: 수확기(8~9월) 동안 하루 최저기온의 평균. 익는 시기 밤 기온
unit: "°C"
dataset: MERRA-2
source: NASA POWER 일별 T2M_MIN
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 수확기 (8~9월, 남반구 2~3월)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
station_var: tmin
keywords: [수확기 밤, 최저기온, 서늘한 밤, 색, 향]
---

## 정의
수확기 동안 하루 최저기온을 평균한 값입니다.

## 왜 중요한가
익는 시기 밤이 서늘해야 색과 향, 산도가 지켜집니다. 서늘한 밤 지수(9월 한 달)보다 긴 두 달을 봐서 그해 차이에 덜 흔들립니다.

## 해석 가이드
- 기울기가 양수면 익는 시기 밤이 따뜻해지는 쪽입니다.

## 주의점
- 50km 격자 평균이라 고도·경사면 차이는 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
