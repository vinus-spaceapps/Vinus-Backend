---
id: summer_solar
name: 여름 일사량
category: sun_wind
order: 30
short: 여름 한 달(7월, 남반구 1월) 동안 땅에 닿은 햇빛 에너지의 하루 평균
unit: "MJ/m²·일"
dataset: CERES
source: NASA POWER 일별 ALLSKY_SFC_SW_DWN (CERES)
start_year: 2001
resolution: 약 100km (CERES 1° 격자)
stage: 여름 (7월, 남반구 1월)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
keywords: [햇빛, 여름, 장마, 흐림, 광합성]
---

## 정의
여름 한 달 동안 하루 일사량(MJ/m²)을 평균한 값입니다.

## 왜 중요한가
알이 크는 여름의 햇빛은 광합성 양을 정합니다. 장마로 흐린 여름이 잦은 산지에서 수확량·품질 변동을 설명하는 데 씁니다.

## 해석 가이드
- 기울기가 음수면 여름이 흐려지는 쪽입니다.

## 주의점
- CERES 1° 격자 값입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
