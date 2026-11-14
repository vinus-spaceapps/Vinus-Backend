---
id: water_balance_harvest
name: 수확기 물수지
category: drought
order: 30
short: 수확기(8~9월) 동안 내린 비에서 증발로 잃는 물을 뺀 값
unit: "mm"
dataset: MERRA-2
source: NASA POWER 일별 T2M·T2M_MAX·T2M_MIN·PRECTOTCORR
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 수확기 (8~9월, 남반구 2~3월)
condition: Σ (강수량 − 기준 증발산량 ET0), Hargreaves 식
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: neutral
keywords: [수확기 물, 물수지, 묽은 맛, 관수, 건조]
---

## 정의
수확기 동안 매일 (강수량 − 기준 증발산량)을 더한 값입니다.

## 왜 중요한가
익는 시기에 물이 넘치면 맛이 묽어지고 썩기 쉽고, 너무 모자라면 포도알이 쪼그라듭니다. 수확 직전 관수와 수확 시기 판단에 씁니다.

## 해석 가이드
- 양수면 비가 증발보다 많고(축축함), 음수면 물이 모자람입니다.

## 주의점
- Hargreaves 식은 습한 곳에서 증발산을 크게 잡는 경향이 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
