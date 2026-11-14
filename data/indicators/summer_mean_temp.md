---
id: summer_mean_temp
name: 여름 평균기온
category: growth
order: 100
short: 여름 한 달(7월, 남반구 1월)의 하루 평균기온. 알이 크고 착색을 준비하는 시기
unit: "°C"
dataset: MERRA-2
source: NASA POWER 일별 T2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 여름 (7월, 남반구 1월)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [여름, 7월, 착색, 알 비대, 숙성 속도]
---

## 정의
여름 한 달(7월, 남반구 1월) 동안 하루 평균기온을 평균한 값입니다.

## 왜 중요한가
알이 커지는 시기의 기온은 착색 시작 시점과 숙성 속도를 정합니다. 수확 시기 예측과 품종 적합성 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 여름이 더워지는 쪽입니다.

## 주의점
- 50km 격자 평균이라 고도·경사면 차이는 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
