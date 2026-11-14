---
id: harvest_solar
name: 수확기 일사량
category: sun_wind
order: 20
short: 수확기(8~9월) 동안 땅에 닿은 햇빛 에너지의 하루 평균
unit: "MJ/m²·일"
dataset: CERES
source: NASA POWER 일별 ALLSKY_SFC_SW_DWN (CERES)
start_year: 2001
resolution: 약 100km (CERES 1° 격자)
stage: 수확기 (8~9월, 남반구 2~3월)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
keywords: [햇빛, 일사량, 수확기, 당, 색, 일소]
---

## 정의
수확기 동안 하루 일사량(MJ/m²)을 평균한 값입니다. NASA CERES 위성 자료입니다.

## 왜 중요한가
익는 시기 햇빛은 당과 색을 만들지만 너무 강하면 송이가 탑니다. 잎 따기 정도와 차광 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 익는 시기가 더 맑아지는 쪽입니다.

## 주의점
- CERES 1° 격자 값입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
