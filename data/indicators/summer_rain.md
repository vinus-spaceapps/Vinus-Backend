---
id: summer_rain
name: 여름 강수량
category: rain_water
order: 100
short: 여름 한 달(7월, 남반구 1월) 동안 내린 비의 총량. 알이 크는 시기의 물
unit: "mm"
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 여름 (7월, 남반구 1월)
condition: (조건 없음) 기간 합계
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: neutral
keywords: [여름비, 장마, 7월, 알 비대, 배수]
---

## 정의
포도알이 커지는 여름 한 달(7월, 남반구 1월) 동안 내린 비를 모두 더한 양입니다.

## 왜 중요한가
이 시기 비가 너무 많으면 알이 커져 맛이 묽어지고 병이 번지며, 너무 적으면 알이 작아집니다. 장마가 7월에 걸리는 영동에서 특히 중요해 관수·배수 판단에 씁니다.

## 해석 가이드
- 해마다 차이가 큽니다. 여름 물수지와 함께 보세요.

## 주의점
- MERRA-2 강수는 모델에 관측을 보정한 값이라 국지성 비를 작게 잡을 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
