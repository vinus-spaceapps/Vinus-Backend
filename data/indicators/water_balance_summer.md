---
id: water_balance_summer
name: 여름 물수지
category: drought
order: 20
short: 여름 두 달(7~8월) 동안 내린 비에서 증발로 잃는 물을 뺀 값. 착색 전후의 물 부족
unit: "mm"
dataset: MERRA-2
source: NASA POWER 일별 T2M·T2M_MAX·T2M_MIN·PRECTOTCORR
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 여름 (7~8월, 남반구 1~2월)
condition: Σ (강수량 − 기준 증발산량 ET0), Hargreaves 식
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: better
keywords: [여름 가뭄, 물수지, 물 스트레스, 관수, 착색]
---

## 정의
여름 두 달(7~8월, 남반구 1~2월) 동안 매일 (강수량 − 기준 증발산량)을 더한 값입니다.

## 왜 중요한가
착색 전후의 적당한 물 부족은 품질을 높이지만, 너무 심하면 잎이 지고 숙성이 멈춥니다. 이 시기 관수를 할지 판단하는 데 가장 직접적입니다.

## 해석 가이드
- 기울기가 음수면 여름 물 부족이 심해지는 쪽입니다.

## 주의점
- Hargreaves 식은 습한 곳에서 증발산을 크게 잡는 경향이 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
