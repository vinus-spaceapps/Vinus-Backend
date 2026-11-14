---
id: ripening_night_lst
name: 착색기 밤 지표면 온도
category: growth
short: 착색부터 수확까지 위성이 잰 밤 지표면 온도의 평균
unit: °C
dataset: MODIS
source: MODIS Terra/Aqua MOD11A1·MYD11A1 LST_Night_1km
start_year: 2003
resolution: 1km (산지 영역 평균)
stage: 착색~수확
stage_from: veraison
stage_to: harvest
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
keywords: [밤, 야간, 열대야, 밤 기온, 일교차, 산도, 색, 착색, 안토시아닌, 지표면 온도, night]
---

## 정의
포도 색이 들기 시작한 날부터 수확일까지, MODIS 위성이 밤에 잰 땅 표면 온도를 평균한 값입니다.

## 왜 중요한가
익어 가는 시기의 밤이 서늘해야 포도가 산도와 색을 지킵니다. 밤 온도가 오르면 산도가 빠르게 떨어지고 색이 덜 듭니다. 품종 교체, 수확 시기 조정, 고지대 밭 확보를 고민할 때 씁니다.

## 해석 가이드
- 기울기가 양수면 익는 시기의 밤이 더워지는 쪽입니다.
- 지표면 온도는 공기 온도보다 밤에 몇 도 낮게 나오는 경우가 많습니다. 절대값보다 변화 방향을 보세요.

## 주의점
- 구름 낀 밤은 값이 비어 있어 맑은 밤 위주로 평균됩니다.
- 지표면 온도(LST)는 2m 기온과 다른 물리량입니다.

## 근거
- Wan, Z. (2014), New refinements and validation of the collection-6 MODIS land-surface temperature/emissivity product — https://doi.org/10.1016/j.rse.2013.08.027
