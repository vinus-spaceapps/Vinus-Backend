---
id: gs_solar
name: 생육기 일사량
category: sun_wind
order: 10
short: 생육기 동안 땅에 닿은 햇빛 에너지의 하루 평균
unit: MJ/m²·일
dataset: CERES
source: NASA POWER 일별 ALLSKY_SFC_SW_DWN (CERES 위성 지표 일사량)
start_year: 2001
resolution: 약 100km (CERES 1° 격자)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
keywords: [햇빛, 일사량, 일조, 맑은 날, 구름, 광합성, 일소]
---

## 정의
생육기 동안 구름을 포함한 실제 날씨에서 땅 1m²에 하루에 닿은 햇빛 에너지(MJ)를 평균한 값입니다. NASA CERES 위성 자료를 NASA POWER가 일별로 제공합니다.

## 왜 중요한가
햇빛은 광합성과 당 축적의 원천입니다. 일사량이 늘면 숙성은 빨라지지만 일소(햇볕 데임) 위험도 커져, 잎 관리(엽면 관리)와 차광망 투자 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 맑은 날이 늘거나 구름이 줄어드는 쪽입니다.

## 주의점
- MERRA-2가 아니라 CERES 자료입니다. 최근 며칠은 아직 값이 없습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
- NASA CERES — https://ceres.larc.nasa.gov/
