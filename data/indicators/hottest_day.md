---
id: hottest_day
name: 생육기 최고기온
category: heat
order: 40
short: 생육기 중 가장 더웠던 날의 최고기온
unit: "°C"
dataset: MERRA-2
source: NASA POWER 일별 T2M_MAX
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: (조건 없음) 기간 중 최고기온의 최댓값
threshold:
threshold_unit:
threshold_options: []
aggregation: max
robust: false
higher_is: worse
station_var: tmax
keywords: [최고기온, 가장 더운 날, 폭염, 극한 더위, 일소]
---

## 정의
생육기 동안 하루 최고기온 가운데 가장 높은 값입니다.

## 왜 중요한가
한 번의 극단적인 더위(40°C 안팎)로도 잎이 타고 포도알이 익어 버릴 수 있습니다. 차광망·관수 같은 폭염 대비 투자 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 가장 더운 날이 더 뜨거워지는 쪽입니다.

## 주의점
- 50km 격자 평균이라 고도·경사면 차이는 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
