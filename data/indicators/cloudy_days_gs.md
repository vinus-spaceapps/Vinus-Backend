---
id: cloudy_days_gs
name: 생육기 흐린 날수
category: sun_wind
order: 60
short: 생육기 동안 구름이 짙어 햇빛이 크게 모자랐던 날 수
unit: "일"
dataset: CERES
source: NASA POWER 일별 ALLSKY_SFC_SW_DWN (CERES)
start_year: 2001
resolution: 약 100km (CERES 1° 격자)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: 일사량 < 맑은 날 일사량(0.75 × 대기 상단 일사량)의 40%
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [흐린 날, 구름, 장마, 일조 부족, 당도]
---

## 정의
생육기 동안 실제 일사량이 그날 맑은 하늘에서 받을 수 있는 일사량의 40% 미만이었던 날의 수입니다.

## 왜 중요한가
흐린 날이 이어지면 광합성이 줄어 당이 덜 오르고 잎이 오래 젖어 병이 번집니다. 장마가 긴 산지의 품질 변동과 방제 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 흐린 날이 늘어나는 쪽입니다.

## 주의점
- CERES 1° 격자 값입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
