---
id: max_daily_rain
name: 생육기 최대 일강수량
category: rain_water
order: 140
short: 생육기 동안 하루에 가장 많이 내린 비의 양. 집중호우의 세기
unit: mm
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR (MERRA-2 관측 보정 강수)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: (조건 없음) 기간 중 하루 강수량 최댓값
threshold:
threshold_unit:
threshold_options: []
aggregation: max
robust: false
higher_is: worse
keywords: [집중호우, 폭우, 호우, 하루 최대, 침수, 토양 유실, 태풍]
---

## 정의
생육기 동안 하루 강수량 가운데 가장 큰 값입니다.

## 왜 중요한가
한 번의 집중호우는 경사면 밭의 흙을 쓸어가고 송이를 터뜨리며 배수 시설을 넘칩니다. 배수로·경사면 관리 투자와 보험 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 집중호우가 세지는 쪽입니다. 해마다 출렁임이 커서 극단값 연도를 함께 보세요.

## 주의점
- 50km 격자 모델 강수는 국지성 집중호우를 크게 줄여 잡습니다. 실제 밭의 최대 강수는 더 클 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
