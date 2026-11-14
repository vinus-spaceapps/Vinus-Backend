---
id: spring_wet_days
name: 봄 비 온 날수
category: rain_water
order: 90
short: 봄(4~5월) 동안 비(1mm 이상)가 온 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 봄 (4/1~5/31, 남반구 10/1~11/30)
condition: 일 강수량 ≥ 1mm
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [봄비, 비 오는 날, 노균병, 탄저병, 방제]
---

## 정의
봄 두 달 동안 하루 강수량이 1mm 이상이었던 날의 수입니다.

## 왜 중요한가
새순과 어린 잎이 자주 젖으면 노균병·탄저병이 시작됩니다. 비의 양보다 '자주'가 병에 중요해 첫 방제 일정에 씁니다.

## 해석 가이드
- 기울기가 양수면 봄비가 잦아지는 쪽입니다.

## 주의점
- 모델 강수는 약한 비를 실제보다 자주 내리는 경향이 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
