---
id: gs_tmax_mean
name: 생육기 평균 최고기온
category: heat
order: 50
short: 생육기 동안 하루 최고기온의 평균. 낮 더위의 수준
unit: "°C"
dataset: MERRA-2
source: NASA POWER 일별 T2M_MAX
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
station_var: tmax
keywords: [낮 기온, 최고기온, 한낮, 더위, 광합성]
---

## 정의
생육기 동안 하루 최고기온을 평균한 값입니다.

## 왜 중요한가
평균기온이 같아도 낮이 더 뜨거워지면 한낮 광합성이 멈추는 시간이 늘어납니다. 낮 더위가 오르는지 밤 기온이 오르는지 구분할 때 생육기 평균 최저기온과 함께 씁니다.

## 해석 가이드
- 기울기가 양수면 낮이 더워지는 쪽입니다.

## 주의점
- 50km 격자 평균이라 고도·경사면 차이는 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
