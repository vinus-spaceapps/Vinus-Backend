---
id: dry_air_days
name: 건조한 날수
category: drought
order: 70
short: 생육기 동안 하루 평균 습도가 40% 미만으로 메마른 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 RH2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: 일평균 상대습도 < 40%
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [건조, 낮은 습도, 메마른, 일소, 수분 스트레스]
---

## 정의
생육기 동안 하루 평균 상대습도가 40% 미만이었던 날의 수입니다.

## 왜 중요한가
공기가 메마르면 잎과 포도알에서 물이 빨리 빠져 알이 작아지고 일소 피해가 커집니다. 다만 병은 줄어듭니다. 관수·차광 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 메마른 날이 늘어나는 쪽입니다.

## 주의점
- 하루 평균값으로 계산한 근사입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
