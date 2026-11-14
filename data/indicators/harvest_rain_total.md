---
id: harvest_rain_total
name: 수확기 강수량
category: rain_water
order: 10
short: 수확기(8~9월, 남반구 2~3월) 동안 내린 비의 총량
unit: mm
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR (MERRA-2 관측 보정 강수)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 수확기 (8~9월, 남반구 2~3월)
stage_from: veraison
stage_to: harvest
condition: (조건 없음) 기간 합계
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: worse
keywords: [비, 강수량, 장마, 습해, 곰팡이, 노균병, 수확 지연, 태풍, rain, precipitation]
---

## 정의
수확기(북반구 8~9월, 남반구 2~3월) 두 달 동안 내린 비를 모두 더한 양입니다.

## 왜 중요한가
수확기에 비가 많으면 곰팡이병이 번지고 포도가 물을 머금어 맛이 묽어지며, 수확이 늦어집니다(보르도 2024). 수확 계획, 방제 일정, 비가림 시설 투자에 씁니다.

## 해석 가이드
- 기울기가 양수면 수확기가 더 축축해지는 쪽입니다.
- 장마·태풍이 있는 영동은 해마다 차이가 매우 커서 한두 해가 추세를 좌우할 수 있습니다.

## 주의점
- MERRA-2 강수는 모델에 관측을 보정한 값입니다. GPM IMERG(약 10km)로 교차 확인할 계획입니다.

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) 3_산지좌표(보르도 2024 강우·곰팡이병), 7_연도별지표
- NASA POWER — https://power.larc.nasa.gov/
