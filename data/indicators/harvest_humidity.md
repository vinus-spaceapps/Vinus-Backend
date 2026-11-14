---
id: harvest_humidity
name: 수확기 평균 습도
category: disease
order: 60
short: 수확기(8~9월, 남반구 2~3월) 하루 평균 상대습도의 평균
unit: "%"
dataset: MERRA-2
source: NASA POWER 일별 RH2M (MERRA-2 2m 상대습도)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 수확기 (8~9월, 남반구 2~3월)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
keywords: [습도, 눅눅, 수확기, 곰팡이, 잿빛곰팡이, 부패, 열과]
---

## 정의
수확기 동안 하루 평균 상대습도를 평균한 값입니다.

## 왜 중요한가
익은 포도는 습할 때 잿빛곰팡이병으로 쉽게 썩습니다. 수확 시기 결정, 수확 전 방제, 비가림 시설 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 수확기가 더 눅눅해지는 쪽입니다. 수확기 강수량·호우일수와 함께 보세요.

## 주의점
- 일평균이라 밤 이슬이나 안개는 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
