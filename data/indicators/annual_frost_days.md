---
id: annual_frost_days
name: 연간 서리일수
category: temp_frost
order: 90
short: 시즌 1년 동안 최저기온이 0°C 이하였던 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 T2M_MIN
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 시즌 1년 (전년 10월~9월, 남반구 전년 4월~3월)
condition: 일 최저기온 ≤ 0°C
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
station_var: tmin
keywords: [서리, 영하, 서리일, 추위, 연간]
---

## 정의
시즌 1년(전년 10월~9월, 남반구 전년 4월~3월) 동안 하루 최저기온이 0°C 이하였던 날의 수입니다.

## 왜 중요한가
산지의 전반적인 추위 정도를 보여 주는 가장 단순한 지표입니다. 서리일수가 크게 줄면 그 산지의 재배 가능 품종 폭이 넓어집니다.

## 해석 가이드
- 기울기가 음수면 서리가 내리는 날이 줄어드는 쪽입니다. 봄 서리 지표와 같이 보면 '서리가 언제 줄었는지' 알 수 있습니다.

## 주의점
- 오카나간은 격자 기온이 관측소보다 약 5°C 낮아 추위 지표가 부풀 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
