---
id: flowering_rain
name: 개화기 강수량
category: rain_water
order: 60
short: 꽃이 피는 달(6월, 남반구 12월)에 내린 비의 총량. 비가 많으면 열매가 덜 맺힘
unit: mm
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR (MERRA-2 관측 보정 강수)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 개화기 (6월, 남반구 12월)
condition: (조건 없음) 기간 합계
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: worse
keywords: [개화, 꽃, 착과, 꽃떨이, 장마, 비, 수확량]
---

## 정의
포도꽃이 피는 달(북반구 6월, 남반구 12월)에 내린 비를 모두 더한 양입니다.

## 왜 중요한가
꽃이 필 때 비가 오면 꽃가루가 씻겨 열매가 덜 맺히고(꽃떨이) 송이가 성기게 됩니다. 장마가 6월에 시작되는 영동처럼 개화기와 장마가 겹치는 산지에서 수확량 예측과 품종 선택에 씁니다.

## 해석 가이드
- 기울기가 양수면 개화기가 축축해지는 쪽입니다.

## 주의점
- 실제 개화 시기와 장마 시작이 해마다 달라 한 달 고정 기간은 근사입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
