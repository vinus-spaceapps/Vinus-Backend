---
id: flowering_solar
name: 개화기 일사량
category: sun_wind
order: 40
short: 꽃이 피는 달(6월) 동안 땅에 닿은 햇빛 에너지의 하루 평균
unit: "MJ/m²·일"
dataset: CERES
source: NASA POWER 일별 ALLSKY_SFC_SW_DWN (CERES)
start_year: 2001
resolution: 약 100km (CERES 1° 격자)
stage: 개화기 (6월, 남반구 12월)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: better
keywords: [개화, 착과, 햇빛, 흐림, 꽃떨이]
---

## 정의
개화기 동안 하루 일사량(MJ/m²)을 평균한 값입니다.

## 왜 중요한가
꽃이 필 때 흐린 날이 이어지면 탄수화물이 부족해 열매가 덜 맺힙니다. 개화기 기온·비와 함께 그해 착과를 가늠하는 데 씁니다.

## 해석 가이드
- 기울기가 양수면 개화기가 맑아지는 쪽입니다.

## 주의점
- CERES 1° 격자 값입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
