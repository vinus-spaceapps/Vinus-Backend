---
id: flowering_wet_days
name: 개화기 비 온 날수
category: rain_water
order: 70
short: 꽃이 피는 달(6월) 동안 비(1mm 이상)가 온 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 개화기 (6월, 남반구 12월)
condition: 일 강수량 ≥ 1mm
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [개화, 꽃떨이, 착과, 비, 수확량]
---

## 정의
개화기 동안 하루 강수량이 1mm 이상이었던 날의 수입니다.

## 왜 중요한가
꽃이 필 때 비가 자주 오면 꽃가루받이가 안 돼 열매가 덜 맺힙니다(꽃떨이). 개화기 강수량(양)과 함께 그해 수확량을 가늠하는 데 씁니다.

## 해석 가이드
- 기울기가 양수면 개화기 비가 잦아지는 쪽입니다.

## 주의점
- 실제 개화 시기는 해마다 달라 한 달 고정 기간은 근사입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
