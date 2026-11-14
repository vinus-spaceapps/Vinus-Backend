---
id: tropical_nights
name: 생육기 열대야일수
category: heat
order: 60
short: 생육기 동안 밤에도 최저기온이 기준값(기본 20°C) 이상이었던 날 수
unit: 일
dataset: MERRA-2
source: NASA POWER 일별 T2M_MIN (MERRA-2 2m 최저기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: 일 최저기온 ≥ 기준값
threshold: 20
threshold_unit: °C
threshold_options: [18, 20, 22]
aggregation: count
robust: false
higher_is: worse
station_var: tmin
keywords: [열대야, 밤 더위, 밤 기온, 더운 밤, 산도, 향, 호흡]
---

## 정의
생육기 동안 하루 최저기온이 기준값(기본 20°C) 이상, 즉 밤에도 덥던 날의 수입니다. 18°C·22°C로 바꿔 볼 수 있습니다.

## 왜 중요한가
밤이 더우면 포도가 밤사이 호흡으로 산(사과산)을 소모해 산도가 빨리 떨어지고 향이 약해집니다. 품종 교체, 수확 시기 조정, 고지대 밭 확보를 고민할 때 씁니다.

## 해석 가이드
- 기울기가 양수면 더운 밤이 늘어나는 쪽입니다.
- 서늘한 유럽 산지는 거의 0입니다. 영동처럼 여름이 무더운 산지에서 의미가 큽니다.

## 주의점
- 격자 최저기온 오차가 있는 산지는 근처 관측소 비교를 함께 보세요.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
