---
id: greenup_doy
name: 싹트는 날짜 (그린업)
category: growth
order: 190
short: 위성이 본 그해 식생이 초록으로 돌아오기 시작한 날 (1월 1일부터 센 날짜)
unit: 연중일
dataset: MODIS
source: MODIS MCD12Q2 Land Cover Dynamics, Greenup (산지 영역 500m 픽셀 중앙값)
start_year: 2001
resolution: 500m (산지 영역 픽셀 중앙값)
stage: 연 1회
stage_from: budburst
stage_to: budburst
condition: (조건 없음) 연 1회 날짜
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
keywords: [발아, 싹, 그린업, 봄, 개엽, 생육 시작, 빨라, 앞당겨, 일찍, phenology, greenup]
---

## 정의
MODIS 위성이 본 그해 식생이 초록으로 돌아오기 시작한 날짜를, 1월 1일을 1로 세어 나타낸 값입니다(예: 80 = 3월 하순). 산지 영역 500m 픽셀들의 중앙값입니다.

## 왜 중요한가
싹이 일찍 트면 그 뒤에 오는 늦서리에 새순이 노출되는 기간이 길어집니다. "따뜻해졌는데 서리 피해는 왜 그대로인가"를 설명하는 열쇠이고, 싹튼 뒤 서리일수의 계산 시작점이기도 합니다.

## 해석 가이드
- 기울기가 음수면 싹트는 날이 앞당겨지는 쪽입니다. 싹튼 뒤 서리일수와 함께 보세요.

## 주의점
- 포도밭만이 아니라 산지 영역의 모든 식생(풀·숲 포함)을 반영합니다.
- 남반구(바로사)는 겨울 목초가 먼저 초록이 되어 날짜가 포도 발아(9월)와 다르게 잡힐 수 있습니다.
- 구름·눈이 많은 해는 유효 픽셀 수가 적습니다.

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) 8_MODIS그린업
- Friedl et al., MCD12Q2 v6.1 — https://doi.org/10.5067/MODIS/MCD12Q2.061
