---
id: wet_spell_max_gs
name: 생육기 최장 연속 강우일
category: rain_water
order: 170
short: 생육기 동안 비 오는 날이 가장 길게 이어진 일수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: 일 강수량 ≥ 1mm 인 날이 가장 길게 이어진 기간
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [장마, 연속 강우, 방제, 병, 잎 젖음]
---

## 정의
생육기 동안 하루 강수량 1mm 이상인 날이 가장 길게 연속된 날 수입니다.

## 왜 중요한가
비가 며칠씩 이어지면 방제를 할 틈이 없고 잎이 계속 젖어 병이 폭발적으로 번집니다. 방제 계획과 내병성 품종 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 긴 장마가 늘어나는 쪽입니다.

## 주의점
- 모델 강수는 약한 비를 실제보다 자주 내리는 경향이 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
