---
id: harvest_max_rain
name: 수확기 최대 일강수량
category: rain_water
order: 40
short: 수확기(8~9월) 중 하루에 가장 많이 내린 비의 양
unit: "mm"
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 수확기 (8~9월, 남반구 2~3월)
condition: (조건 없음) 기간 중 하루 강수량 최댓값
threshold:
threshold_unit:
threshold_options: []
aggregation: max
robust: false
higher_is: worse
keywords: [수확기 폭우, 태풍, 집중호우, 열과, 터짐]
---

## 정의
수확기 동안 하루 강수량 가운데 가장 큰 값입니다.

## 왜 중요한가
익은 포도는 한 번의 폭우에도 터지고(열과) 썩기 시작합니다. 태풍·집중호우가 수확기에 오는 산지의 보험·수확 계획에 씁니다.

## 해석 가이드
- 해마다 출렁임이 커서 극단값 연도를 함께 보세요.

## 주의점
- 50km 격자 모델 강수는 국지성 집중호우를 크게 줄여 잡습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
