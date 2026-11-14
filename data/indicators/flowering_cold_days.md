---
id: flowering_cold_days
name: 개화기 저온일수
category: growth
order: 90
short: 꽃이 피는 달(6월) 동안 평균기온이 15°C 아래로 서늘했던 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 T2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 개화기 (6월, 남반구 12월)
condition: 일 평균기온 < 15°C
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
station_var: tmean
keywords: [개화, 저온, 꽃떨이, 착과, 서늘]
---

## 정의
개화기 동안 하루 평균기온이 15°C 미만이었던 날의 수입니다.

## 왜 중요한가
꽃이 필 때 서늘하면 꽃가루받이가 늦어지고 열매가 덜 맺혀(꽃떨이) 송이가 성기게 됩니다. 서늘한 산지의 수확량 예측과 품종 선택에 씁니다.

## 해석 가이드
- 기울기가 음수면 개화기 저온이 줄어드는 쪽입니다.

## 주의점
- 실제 개화 시기는 해마다 달라 한 달 고정 기간은 근사입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
