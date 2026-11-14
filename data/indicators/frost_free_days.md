---
id: frost_free_days
name: 무상기간
category: growth
order: 230
short: 마지막 봄 서리와 첫 가을 서리 사이, 서리가 없는 날의 수
unit: 일
dataset: MERRA-2
source: NASA POWER 일별 T2M_MIN (MERRA-2 2m 최저기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 마지막 봄 서리 ~ 첫 가을 서리
condition: 일 최저기온 ≤ 0°C 인 날 사이의 기간
threshold: 0
threshold_unit: °C
threshold_options: [0]
aggregation: count
robust: false
higher_is: better
station_var: tmin
keywords: [무상기간, 서리 없는, 생육 기간, 가을 서리, 첫서리, 늦서리, 재배 기간]
---

## 정의
그해 마지막 봄 서리(최저기온 0°C 이하) 다음 날부터 첫 가을 서리 전날까지의 날 수입니다.

## 왜 중요한가
서리 없는 기간이 길어야 늦게 익는 품종도 서리 전에 수확할 수 있습니다. 만생종 도입이나 수확 시기 조정을 고민할 때 씁니다.

## 해석 가이드
- 기울기가 양수면 서리 없는 기간이 길어지는 쪽입니다.

## 주의점
- 서리가 거의 없는 산지(나파 일부 해, 바로사)는 계산되지 않는 해가 많습니다.
- 마지막 연도는 가을이 끝나지 않아 빠질 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
