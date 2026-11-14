---
id: gs_wet_days
name: 생육기 비 온 날수
category: rain_water
order: 120
short: 생육기 동안 하루 강수량이 기준값(기본 1mm) 이상인 날 수
unit: 일
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR (MERRA-2 관측 보정 강수)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: 일 강수량 ≥ 기준값
threshold: 1
threshold_unit: mm
threshold_options: [1, 5, 10]
aggregation: count
robust: false
higher_is: worse
keywords: [비 오는 날, 강우일, 잦은 비, 습한, 곰팡이, 방제, 병]
---

## 정의
생육기 동안 하루 강수량이 기준값(기본 1mm) 이상이었던 날의 수입니다. 5mm·10mm로 바꿔 볼 수 있습니다.

## 왜 중요한가
비의 총량보다 비가 "자주" 오는 것이 곰팡이병에 더 큰 영향을 줍니다. 잎이 자주 젖으면 병이 번지기 때문입니다. 방제 횟수와 비용을 계획할 때 씁니다.

## 해석 가이드
- 기울기가 양수면 비가 잦아지는 쪽입니다. 생육기 고습일수와 함께 보세요.

## 주의점
- 모델 강수는 약한 비를 실제보다 자주 내리는 경향이 있어 1mm 기준은 날 수가 많게 나올 수 있습니다. 5mm 기준도 함께 보세요.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
