---
id: gs_tmin_mean
name: 생육기 평균 최저기온
category: growth
order: 150
short: 생육기 동안 하루 최저기온의 평균. 밤 기온의 수준
unit: "°C"
dataset: MERRA-2
source: NASA POWER 일별 T2M_MIN
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
station_var: tmin
keywords: [밤 기온, 최저기온, 산도, 향, 온난화]
---

## 정의
생육기 동안 하루 최저기온을 평균한 값입니다.

## 왜 중요한가
온난화는 낮보다 밤을 더 빨리 데우는 경우가 많습니다. 밤이 따뜻해지면 산도와 향이 줄어 품질에 영향이 크므로 생육기 평균 최고기온과 함께 씁니다.

## 해석 가이드
- 기울기가 양수면 밤이 따뜻해지는 쪽입니다.

## 주의점
- 50km 격자 평균이라 고도·경사면 차이는 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
