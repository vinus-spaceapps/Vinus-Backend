---
id: thermal_gs_end
name: 생육 종료일 (기온 기준)
category: growth
order: 210
short: 8월 이후 평균기온 10°C 미만이 5일 이어진 첫날. 기온상의 생육 끝
unit: "연중일"
dataset: MERRA-2
source: NASA POWER 일별 T2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 8~12월 (남반구 2~7월)
condition: 평균기온 < 10°C 가 5일 이어진 첫날
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [생육 종료, 가을, 늦가을, 만생종, 기온]
---

## 정의
8월 1일(남반구 2월 1일) 이후 하루 평균기온이 10°C 미만인 날이 처음으로 5일 연속된 날의 첫날입니다.

## 왜 중요한가
이 날이 늦어지면 늦게 익는 품종도 기온상 다 익을 여유가 생기지만 가지가 여무는 시기도 늦어집니다. 만생종 도입과 월동 준비 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 생육 종료가 늦어지는 쪽입니다.

## 주의점
- 그해 가을이 끝나지 않은 마지막 연도는 빠질 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
