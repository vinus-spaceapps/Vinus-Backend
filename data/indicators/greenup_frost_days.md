---
id: greenup_frost_days
name: 그린업 뒤 서리일수
category: temp_frost
order: 20
short: 위성이 본 그해 싹트는 날짜(그린업)부터 30일 동안 최저기온이 기준값 이하였던 날 수
unit: 일
dataset: MERRA-2
source: NASA POWER 일별 T2M_MIN (MERRA-2) + MODIS MCD12Q2 그린업 날짜
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 그해 그린업 날짜부터 30일
condition: 일 최저기온 ≤ 기준값
threshold: 0
threshold_unit: °C
threshold_options: [0, -2]
aggregation: count
robust: false
higher_is: worse
station_var: tmin
keywords: [그린업, 발아 후 서리, 싹튼 뒤, 늦서리, 새순, 냉해, 서리 피해]
---

## 정의
MODIS 위성이 잡은 그해 싹트는 날짜(그린업)부터 30일 동안 하루 최저기온이 기준값(기본 0°C) 이하였던 날의 수입니다. 달력으로 고정한 '싹튼 뒤 서리일수'와 달리, 해마다 달라지는 싹트는 날짜를 따라 기간이 움직입니다.

## 왜 중요한가
온난화로 싹이 빨리 트면 달력상 서리는 줄어도 '싹이 튼 뒤'의 서리는 그대로이거나 늘 수 있습니다. 새순이 실제로 노출되는 서리를 보므로 서리 대비 시설·보험 판단에 더 직접적입니다.

## 해석 가이드
- 기울기가 양수면 새순이 서리를 맞는 날이 늘어나는 쪽입니다.
- 달력 고정 '싹튼 뒤 서리일수'와 방향이 다르면, 싹트는 날짜가 바뀐 효과입니다.

## 주의점
- 그린업은 포도밭만이 아니라 산지 영역 식생 전체의 값입니다.
- 남반구(바로사)는 그린업이 겨울 목초를 잡아 계산하지 않습니다.
- MODIS 그린업이 없는 해(2026년 등)는 빠집니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
