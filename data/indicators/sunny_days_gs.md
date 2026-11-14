---
id: sunny_days_gs
name: 생육기 맑은 날수
category: sun_wind
order: 50
short: 생육기 동안 구름이 거의 없이 맑았던 날 수
unit: "일"
dataset: CERES
source: NASA POWER 일별 ALLSKY_SFC_SW_DWN (CERES)
start_year: 2001
resolution: 약 100km (CERES 1° 격자)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: 일사량 ≥ 맑은 날 일사량(0.75 × 대기 상단 일사량)의 80%
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: neutral
keywords: [맑은 날, 일조, 햇빛, 구름, 날씨]
---

## 정의
생육기 동안 실제 일사량이 그날 맑은 하늘에서 받을 수 있는 일사량(FAO-56 식)의 80% 이상이었던 날의 수입니다.

## 왜 중요한가
맑은 날이 많으면 당과 색이 잘 오르지만 일소와 물 스트레스도 커집니다. 잎 관리·차광·관수 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 맑은 날이 늘어나는 쪽입니다.

## 주의점
- CERES 1° 격자 값입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
