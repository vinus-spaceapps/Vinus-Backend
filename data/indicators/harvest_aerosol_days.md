---
id: harvest_aerosol_days
name: 수확기 연기 에어로졸 일수
category: smoke_air
short: 착색부터 수확까지 자외선 에어로졸 지수(연기·먼지)가 기준값 이상이었던 날 수
unit: 일
dataset: OMI
source: OMI/Aura OMAERUVd 자외선 에어로졸 지수 (UV Aerosol Index)
start_year: 2005
resolution: 1° 격자 (센서 화소 수십 km)
stage: 착색~수확
stage_from: veraison
stage_to: harvest
condition: 자외선 에어로졸 지수 ≥ 기준값
threshold: 1.0
threshold_unit: (지수)
threshold_options: [0.7, 1.0, 1.5]
aggregation: count
robust: true
higher_is: worse
keywords: [에어로졸, 연기, 먼지, 미세먼지, 황사, 연무, 산불, 하늘, aerosol, smoke]
---

## 정의
착색부터 수확일까지, 위성이 잰 자외선 에어로졸 지수가 기준값(기본 1.0) 이상이었던 날의 수입니다. 이 지수는 햇빛을 흡수하는 연기·먼지 입자가 많을수록 커집니다.

## 왜 중요한가
일산화탄소(수확기 연기 노출일수)와 함께 보면 "연기가 실제로 하늘을 덮었는가"를 교차 확인할 수 있습니다. 두 지표가 같은 방향이면 연기 노출 증가 판단에 더 힘이 실립니다.

## 해석 가이드
- 산불 연기처럼 튀는 지표라 Sen 기울기와 Mann-Kendall을 기본으로 봅니다.
- 황사 같은 먼지도 지수를 올리므로 동아시아 산지에서는 봄 먼지와 구분해서 보세요.

## 주의점
- OMI는 2007년부터 센서 일부 구역 손실(row anomaly)이 있어 관측 빈도가 줄었습니다.
- 구름이 많은 날은 값이 비어 날수가 적게 셀 수 있습니다.

## 근거
- Torres et al. (2007), Aerosols and surface UV products from OMI — https://doi.org/10.1029/2007JD008809
