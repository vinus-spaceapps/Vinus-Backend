---
id: spring_rain
name: 봄 강수량
category: rain_water
order: 80
short: 봄(4~5월, 남반구 10~11월)에 내린 비의 총량
unit: "mm"
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 봄 (4/1~5/31, 남반구 10/1~11/30)
condition: (조건 없음) 기간 합계
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: neutral
keywords: [봄비, 봄 강수, 노균병, 새순, 초기 생장]
---

## 정의
봄 두 달 동안 내린 비를 모두 더한 양입니다.

## 왜 중요한가
새순이 자라는 봄에 비가 많으면 노균병이 일찍 시작되고, 너무 적으면 초기 생장이 더딥니다. 첫 방제 시기와 초기 관수 판단에 씁니다.

## 해석 가이드
- 해마다 차이가 커서 극단적인 해를 함께 보세요.

## 주의점
- MERRA-2 강수는 모델에 관측을 보정한 값이라 국지성 비를 작게 잡을 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
