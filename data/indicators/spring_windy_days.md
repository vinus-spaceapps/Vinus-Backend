---
id: spring_windy_days
name: 봄 강풍일수
category: sun_wind
order: 80
short: 생육 초기(4~6월) 동안 하루 평균 풍속이 기준값(기본 5 m/s) 이상인 바람 센 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 WS2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육 초기 (4~6월, 남반구 10~12월)
condition: 일평균 풍속 ≥ 기준값
threshold: 5
threshold_unit: m/s
threshold_options: [4, 5, 6]
aggregation: count
robust: false
higher_is: worse
keywords: [강풍, 센 바람, 새순 꺾임, 방풍, 돌풍]
---

## 정의
생육 초기(4~6월, 남반구 10~12월) 동안 하루 평균 풍속이 기준값(기본 5 m/s) 이상이었던 날의 수입니다. 4·6 m/s로 바꿔 볼 수 있습니다.

## 왜 중요한가
어린 새순은 센 바람에 쉽게 꺾여 그해 송이를 잃습니다. 방풍망·유인(가지 묶기) 작업 시기 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 봄에 센 바람이 잦아지는 쪽입니다.

## 주의점
- 일평균 풍속이라 순간 돌풍은 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
