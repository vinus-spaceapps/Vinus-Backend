---
id: gs_rain_total
name: 생육기 강수량
category: rain_water
order: 110
short: 생육기 동안 내린 비의 총량
unit: mm
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR (MERRA-2 관측 보정 강수)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: (조건 없음) 기간 합계
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: neutral
keywords: [강수량, 비, 가뭄, 물, 관수, 장마, 연 강수]
---

## 정의
생육기 동안 내린 비를 모두 더한 양입니다.

## 왜 중요한가
생육기 비가 너무 적으면 관수가 필요하고, 너무 많으면 병해와 과도한 잎 성장이 생깁니다. 관수 시설 투자와 방제 계획에 씁니다.

## 해석 가이드
- 해마다 차이가 커서 추세보다 극단적인 해(가뭄·장마)를 함께 보세요. 수확기 강수량, 최장 무강수 기간과 같이 보면 비가 "언제" 바뀌었는지 알 수 있습니다.

## 주의점
- MERRA-2 강수는 모델에 관측을 보정한 값이라 국지성 호우를 작게 잡을 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
