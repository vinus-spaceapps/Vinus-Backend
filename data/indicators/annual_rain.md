---
id: annual_rain
name: 연 강수량
category: rain_water
order: 190
short: 시즌 1년(전년 10월~9월) 동안 내린 비의 총량
unit: "mm"
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 시즌 1년 (전년 10월~9월, 남반구 전년 4월~3월)
condition: (조건 없음) 기간 합계
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: neutral
keywords: [연 강수량, 1년 비, 물 사정, 가뭄, 저수]
---

## 정의
시즌 1년(전년 10월~9월, 남반구 전년 4월~3월) 동안 내린 비를 모두 더한 양입니다.

## 왜 중요한가
산지의 물 사정을 보여 주는 가장 기본적인 지표입니다. 연 강수량이 줄면 저수·관수 시설과 물 사용권 확보가 중요해집니다.

## 해석 가이드
- 기울기가 음수면 한 해 비가 줄어드는 쪽입니다. 비가 '언제' 바뀌었는지는 계절별 강수량으로 보세요.

## 주의점
- MERRA-2 강수는 모델에 관측을 보정한 값이라 국지성 비를 작게 잡을 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
