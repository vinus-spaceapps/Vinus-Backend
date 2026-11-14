---
id: harvest_dew_days
name: 수확기 이슬 맺힘 일수
category: disease
order: 80
short: 수확기(8~9월) 동안 밤 기온이 이슬점 가까이 내려가 송이에 이슬이 맺히기 쉬운 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 T2M·RH2M·T2M_MIN
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 수확기 (8~9월, 남반구 2~3월)
condition: 일 최저기온 ≤ 이슬점 + 1°C (이슬점은 평균기온·습도로 계산)
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [이슬, 밤 이슬, 젖음, 곰팡이, 통풍]
---

## 정의
수확기 동안 하루 최저기온이 그날의 이슬점(평균기온·습도로 계산) + 1°C 이하로 내려간 날의 수입니다.

## 왜 중요한가
비가 오지 않아도 밤새 맺힌 이슬로 송이가 젖으면 곰팡이가 번집니다. 송이 주변 잎 따기(통풍)와 방제 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 이슬 맺히는 밤이 늘어나는 쪽입니다.

## 주의점
- 하루 평균값으로 계산한 근사입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
