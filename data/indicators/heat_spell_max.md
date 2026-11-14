---
id: heat_spell_max
name: 최장 폭염 연속일
category: heat
order: 20
short: 생육기 동안 최고기온이 기준값(기본 35°C) 이상인 날이 가장 길게 이어진 일수
unit: 일
dataset: MERRA-2
source: NASA POWER 일별 T2M_MAX (MERRA-2 2m 최고기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: 일 최고기온 ≥ 기준값 인 날이 가장 길게 이어진 기간
threshold: 35
threshold_unit: °C
threshold_options: [30, 35]
aggregation: count
robust: false
higher_is: worse
station_var: tmax
keywords: [폭염, 연속, 열파, 더위 지속, 일소, 잎 마름, 열 스트레스]
---

## 정의
생육기 동안 하루 최고기온이 기준값(기본 35°C) 이상인 날이 가장 길게 연속된 날 수입니다.

## 왜 중요한가
더운 날이 띄엄띄엄 오는 것보다 며칠씩 이어질 때 잎이 마르고 포도알이 쪼그라드는 피해가 큽니다. 차광망·관수 시설과 내열성 품종 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 폭염이 더 길게 이어지는 쪽입니다. 생육기 폭염일수와 함께 보세요.

## 주의점
- 서늘한 산지는 35°C 날이 거의 없어 0인 해가 많습니다. 30°C 기준도 함께 보세요.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
