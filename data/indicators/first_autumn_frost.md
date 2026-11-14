---
id: first_autumn_frost
name: 첫 가을 서리 날
category: temp_frost
order: 80
short: 그해 가을 처음으로 서리(최저기온 0°C 이하)가 내린 날짜 (1월 1일부터 센 날)
unit: 연중일
dataset: MERRA-2
source: NASA POWER 일별 T2M_MIN (MERRA-2 2m 최저기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 7~12월 (남반구 1~6월)
condition: 일 최저기온 ≤ 기준값 인 첫날
threshold: 0
threshold_unit: °C
threshold_options: [0, -2]
aggregation: mean
robust: false
higher_is: better
station_var: tmin
keywords: [첫서리, 가을 서리, 조기 서리, 수확 전 서리, 만생종, 늦게 익는]
---

## 정의
7~12월(남반구 1~6월) 중 하루 최저기온이 기준값 이하였던 첫날을, 1월 1일을 1로 세어 나타낸 값입니다. 예: 300 = 10월 27일 무렵.

## 왜 중요한가
늦게 익는 품종은 첫서리 전에 수확해야 합니다. 첫서리가 늦어지면 만생종이나 아이스와인 같은 선택지가 바뀌므로 품종·수확 계획에 씁니다.

## 해석 가이드
- 기울기가 양수면 첫서리가 늦어지는 쪽입니다. 무상기간과 함께 보세요.

## 주의점
- 그해 가을이 아직 끝나지 않은 마지막 연도와 서리가 없는 해는 빠집니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
