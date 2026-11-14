---
id: heat_days
name: 생육기 폭염일수
category: temp_frost
short: 발아부터 수확까지 최고기온이 기준값 이상이었던 날 수
unit: 일
dataset: MERRA-2
source: MERRA-2 M2SDNXSLV T2MMAX (2m 일 최고기온)
start_year: 1981
resolution: 약 50km
stage: 발아~수확
stage_from: budburst
stage_to: harvest
condition: 일 최고기온 ≥ 기준값
threshold: 35
threshold_unit: °C
threshold_options: [32, 35, 38]
aggregation: count
robust: false
higher_is: worse
keywords: [폭염, 더위, 고온, 열, 일소, 햇볕 데임, 뜨거, 무더위, heat]
---

## 정의
싹이 튼 날부터 수확일까지, 하루 최고기온이 기준값(기본 35°C) 이상이었던 날의 수입니다.

## 왜 중요한가
35°C를 넘는 날이 이어지면 광합성이 멈추고 포도알이 햇볕에 데이며(일소), 산도가 빠르게 떨어집니다. 내열성 품종으로의 교체, 차광망·관수 투자, 수확 시기 조정을 고민할 때 씁니다.

## 해석 가이드
- 기울기가 양수면 고온 스트레스가 늘어나는 쪽입니다.
- 같은 폭염일수라도 착색기 이후에 몰리면 품질 영향이 더 큽니다.

## 주의점
- 50km 격자 평균이라 경사면 방향·고도 차이는 반영되지 않습니다.

## 근거
- Gelaro et al. (2017), MERRA-2 — https://doi.org/10.1175/JCLI-D-16-0758.1
