---
id: rx5day_gs
name: 생육기 5일 최대 강수량
category: rain_water
order: 150
short: 생육기 중 연속 5일 동안 내린 비의 가장 큰 합. 장마·태풍 한 번의 크기
unit: "mm"
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: (조건 없음) 연속 5일 강수량 합의 최댓값
threshold:
threshold_unit:
threshold_options: []
aggregation: max
robust: false
higher_is: worse
keywords: [장마, 태풍, 연속 강수, 침수, 배수]
---

## 정의
생육기 동안 연속 5일 강수량 합 가운데 가장 큰 값입니다.

## 왜 중요한가
하루 폭우보다 며칠 이어진 큰비가 밭을 물에 잠기게 하고 뿌리를 상하게 합니다. 배수 시설 용량과 침수 위험 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 큰비 한 번의 규모가 커지는 쪽입니다.

## 주의점
- MERRA-2 강수는 모델에 관측을 보정한 값이라 국지성 비를 작게 잡을 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
