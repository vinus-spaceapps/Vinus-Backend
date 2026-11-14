---
id: et0_gs
name: 생육기 증발산량
category: drought
order: 40
short: 생육기 동안 땅과 잎에서 증발로 빠져나가는 물의 양(기준 증발산량)의 합
unit: "mm"
dataset: MERRA-2
source: NASA POWER 일별 T2M·T2M_MAX·T2M_MIN
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: Σ 기준 증발산량 ET0 (Hargreaves 식, FAO-56)
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: worse
keywords: [증발산, ET0, 물 수요, 관수량, 건조]
---

## 정의
생육기 동안 매일 기온과 위도로 계산한 기준 증발산량(ET0, Hargreaves 식)을 더한 값입니다.

## 왜 중요한가
기온이 오르면 비가 같아도 증발로 잃는 물이 늘어 관수가 더 필요해집니다. 관수 시설 규모와 물 확보량을 정하는 데 씁니다.

## 해석 가이드
- 기울기가 양수면 대기가 물을 더 많이 빼앗아 가는 쪽입니다.

## 주의점
- 바람·습도를 넣지 않은 식이라 실제 증발산과 차이가 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
