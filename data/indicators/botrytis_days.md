---
id: botrytis_days
name: 잿빛곰팡이 위험일
category: disease
order: 30
short: 수확기(8~9월) 동안 습도 85% 이상, 기온 15~25°C로 잿빛곰팡이가 번지기 좋은 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 T2M·RH2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 수확기 (8~9월, 남반구 2~3월)
condition: 상대습도 ≥ 85% 그리고 15°C ≤ 평균기온 ≤ 25°C
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [잿빛곰팡이, 보트리티스, 부패, 송이 썩음, 수확기 병]
---

## 정의
수확기 동안 하루 평균 상대습도가 85% 이상이고 평균기온이 15~25°C였던 날의 수입니다.

## 왜 중요한가
잿빛곰팡이(보트리티스)는 익은 송이를 통째로 썩게 해 수확 직전 손실을 크게 만듭니다. 수확 시기 앞당김, 수확 전 방제, 송이 솎기 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 수확기 부패 위험이 커지는 쪽입니다.

## 주의점
- 하루 평균값으로 계산한 근사입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
