---
id: harvest_wet_days
name: 수확기 비 온 날수
category: rain_water
order: 30
short: 수확기(8~9월) 동안 비(1mm 이상)가 온 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 수확기 (8~9월, 남반구 2~3월)
condition: 일 강수량 ≥ 1mm
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [수확기 비, 비 오는 날, 잿빛곰팡이, 수확 일정, 비가림]
---

## 정의
수확기 동안 하루 강수량이 1mm 이상이었던 날의 수입니다.

## 왜 중요한가
익은 포도가 자주 젖으면 잿빛곰팡이가 번지고 수확할 날을 잡기 어려워집니다. 수확 인력·일정 계획과 비가림 시설 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 수확기 비가 잦아지는 쪽입니다. 수확기 호우일수(큰비)와 함께 보세요.

## 주의점
- 모델 강수는 약한 비를 실제보다 자주 내리는 경향이 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
