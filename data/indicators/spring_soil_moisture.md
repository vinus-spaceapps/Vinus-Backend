---
id: spring_soil_moisture
name: 봄 토양수분
category: drought
order: 120
short: 봄(4~5월) 동안 뿌리층 흙의 습윤도 평균. 한 해를 시작하는 물
unit: "0~1"
dataset: MERRA-2
source: NASA POWER 일별 GWETROOT
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 봄 (4/1~5/31, 남반구 10/1~11/30)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: better
keywords: [봄 토양, 땅속 물, 초기 생장, 관수 시작]
---

## 정의
봄 두 달 동안 뿌리층 흙의 습윤도를 0~1 사이 값으로 평균한 것입니다.

## 왜 중요한가
봄에 땅속 물이 넉넉해야 새순과 잎이 잘 자랍니다. 봄 토양수분이 낮으면 이른 관수가 필요하므로 관수 시작 시점 판단에 씁니다.

## 해석 가이드
- 기울기가 음수면 봄부터 흙이 마른 채 시작하는 쪽입니다. 휴면기 강수량과 함께 보세요.

## 주의점
- 모델 값입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
