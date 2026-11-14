---
id: gs_soil_moisture
name: 생육기 토양수분
category: rain_water
short: 발아부터 수확까지 겉흙(0~10cm)에 들어 있는 물의 평균량
unit: kg/m²
dataset: GLDAS
source: GLDAS Noah 2.1 SoilMoi0_10cm_inst (0~10cm 토양수분)
start_year: 2001
resolution: 0.25° (약 25km)
stage: 발아~수확
stage_from: budburst
stage_to: harvest
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: better
keywords: [가뭄, 건조, 토양, 흙, 수분, 물 부족, 관수, 물주기, 메마른, drought, soil]
---

## 정의
싹이 튼 날부터 수확일까지, 겉흙 0~10cm 층에 들어 있는 물의 양(1m²당 kg)을 평균한 값입니다.

## 왜 중요한가
포도나무는 적당한 물 스트레스에서 좋은 포도를 맺지만, 너무 마르면 잎이 지고 당 축적이 멈춥니다. 관수 시설 투자, 대목(뿌리) 교체, 내건성 품종 검토에 씁니다.

## 해석 가이드
- 기울기가 음수면 생육기 흙이 점점 마르는 쪽입니다.
- 비가 늘어도 기온이 올라 증발이 늘면 토양수분은 줄 수 있습니다.

## 주의점
- GLDAS 2.0(1948~2014)과 2.1(2000~)은 입력 자료가 달라 이어 붙이지 않습니다. 이 지표는 2.1만 씁니다.
- 모델 값이며 관수한 밭의 실제 토양수분과 다릅니다.

## 근거
- Rodell et al. (2004), The Global Land Data Assimilation System — https://doi.org/10.1175/BAMS-85-3-381
