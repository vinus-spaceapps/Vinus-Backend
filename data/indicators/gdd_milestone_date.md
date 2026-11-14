---
id: gdd_milestone_date
name: 적산온도 도달일
category: growth
order: 50
short: 생육기 시작부터 쌓인 적산온도가 기준값(기본 1,000 °C·일)에 닿은 날. 착색·수확이 얼마나 빨라졌는지
unit: "연중일"
dataset: MERRA-2
source: NASA POWER 일별 T2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 시작(4/1, 남반구 10/1)부터
condition: 적산온도(기준 10°C)가 기준값에 닿은 날
threshold: 1000
threshold_unit: °C·일
threshold_options: [800, 1000, 1200]
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [숙성, 착색, 수확 시기, 빨라진 수확, 적산온도]
---

## 정의
4월 1일(남반구 10월 1일)부터 매일 (평균기온 − 10°C)를 더해, 그 합이 기준값(기본 1,000)에 처음 닿은 날짜입니다(1월 1일부터, 남반구는 7월 1일부터 센 날). 800·1,200으로 바꿔 볼 수 있습니다.

## 왜 중요한가
포도는 쌓인 열이 일정 수준에 이르면 색이 들고 익습니다. 이 날이 앞당겨지면 더 더운 한여름에 익게 되어 품질이 떨어질 수 있으므로, 수확 시기 계획과 품종 교체 판단에 씁니다.

## 해석 가이드
- 기울기가 음수면 같은 열이 더 빨리 쌓여 숙성이 앞당겨지는 쪽입니다.

## 주의점
- 서늘한 산지(오카나간)는 해에 따라 10월 말까지 기준값에 닿지 못해 빠지는 해가 많습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
