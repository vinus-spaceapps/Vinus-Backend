---
id: thermal_gs_length
name: 생육 기간 길이 (기온 기준)
category: growth
order: 220
short: 평균기온 10°C 이상인 기온상 생육 기간의 길이
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 T2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육 시작일 ~ 생육 종료일
condition: 생육 종료일 − 생육 시작일
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: neutral
station_var: tmean
keywords: [생육 기간, 재배 기간, 길이, 품종, 만생종]
---

## 정의
기온 기준 생육 시작일부터 생육 종료일까지의 날 수입니다.

## 왜 중요한가
생육 기간이 길어지면 늦게 익는 품종을 기를 수 있게 되지만, 지금 품종은 너무 빨리 익을 수 있습니다. 품종 교체 판단의 기본 자료입니다.

## 해석 가이드
- 기울기가 양수면 생육 기간이 길어지는 쪽입니다.

## 주의점
- 따뜻한 산지(바로사·나파)는 겨울에도 10°C를 넘어 기간이 매우 길게 나옵니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
