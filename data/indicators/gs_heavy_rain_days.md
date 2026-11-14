---
id: gs_heavy_rain_days
name: 생육기 호우일수
category: rain_water
order: 130
short: 생육기 동안 하루 강수량이 기준값(기본 30mm) 이상인 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: 일 강수량 ≥ 기준값
threshold: 30
threshold_unit: mm
threshold_options: [20, 30, 50]
aggregation: count
robust: false
higher_is: worse
keywords: [호우, 큰비, 집중호우, 토양 유실, 배수]
---

## 정의
생육기 동안 하루 강수량이 기준값(기본 30mm) 이상이었던 날의 수입니다. 20·50mm로 바꿔 볼 수 있습니다.

## 왜 중요한가
큰비는 경사면 밭의 흙을 쓸어가고 병을 퍼뜨리며 배수 시설을 넘칩니다. 배수로·경사면 관리 투자에 씁니다.

## 해석 가이드
- 기울기가 양수면 큰비가 잦아지는 쪽입니다.

## 주의점
- 50km 격자 모델 강수는 국지성 집중호우를 크게 줄여 잡습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
