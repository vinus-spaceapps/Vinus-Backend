---
id: harvest_smoke_days
name: 수확기 연기 노출일수
category: smoke_air
short: 착색부터 수확까지 일산화탄소(연기 지표)가 평소의 기준 배수를 넘은 날 수
unit: 일
dataset: AIRS
source: AIRS L3 일 일산화탄소 총량 (AIRS3STD CO_total_column), 보조로 MERRA-2 지표 유기탄소
start_year: 2003
resolution: 1° (약 100km)
stage: 착색~수확
stage_from: veraison
stage_to: harvest
condition: 일산화탄소 총량 > 2003~2012 같은 날짜 평균 × 기준 배수
threshold: 1.5
threshold_unit: 배
threshold_options: [1.3, 1.5, 2.0]
aggregation: count
robust: true
higher_is: worse
keywords: [연기, 산불, 스모크, 연기 오염, 스모크 테인트, 재, 그을음, 화재, 불, smoke, wildfire, 계약 거절]
---

## 정의
포도 색이 들기 시작한 날(착색)부터 수확일까지, 대기 중 일산화탄소 총량이 그 산지의 평소 수준(2003~2012년 같은 날짜 평균)보다 기준 배수(기본 1.5배) 이상 높았던 날의 수입니다. 일산화탄소는 산불 연기와 함께 이동하는 대표적인 기체입니다.

## 왜 중요한가
착색 이후 연기에 노출된 포도는 와인에서 재 냄새·약품 냄새(스모크 테인트)가 날 수 있어, 와이너리가 계약 물량을 거절하기도 합니다. 2020년 미국 서부에서는 검사 없이 "연기가 있었다"는 이유로 거절된 사례가 있었습니다. 계약 조건·보험·수확 계획을 고민할 때 씁니다.

## 해석 가이드
- 산불 연기는 몇몇 해에 크게 튀므로 Sen 기울기(튀는 해에 덜 흔들림)와 Mann-Kendall 검정을 기본으로 봅니다.
- 추세가 유의해도 특정 한 해가 결과를 만든 것이 아닌지, 가장 튄 해를 뺀 결과를 함께 보세요.

## 주의점
- AIRS는 1° 격자라 산지 하나보다 훨씬 넓은 지역 평균입니다.
- 일산화탄소는 연기의 대리 지표이며, 포도에 실제로 쌓인 휘발성 페놀 양을 뜻하지 않습니다.
- MERRA-2 에어로졸은 2000년대 초 동화 자료가 바뀌어 장기 비교 시 점검이 필요합니다.

## 근거
- 2020년 미국 서부 산불 연기로 인한 와인 생산자 손실 약 6억 달러 추정 — 기획서 v2 문제 정의 표
- AIRS Science Team, AIRS3STD v7 — https://doi.org/10.5067/UO3Q64CTTS1U
