---
id: soil_drought_days
name: 토양 가뭄 일수
category: drought
order: 140
short: 생육기 동안 뿌리층 흙이 그 산지의 평소(2001~2010년) 하위 20%보다 마른 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 GWETROOT
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: 뿌리층 토양수분 < 그 산지 2001~2010년 생육기 하위 20%
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [토양 가뭄, 마른 땅, 가뭄 일수, 관수, 평소보다]
---

## 정의
생육기 동안 뿌리층 토양수분이, 그 산지의 2001~2010년 생육기 값 가운데 하위 20% 기준보다 낮았던 날의 수입니다.

## 왜 중요한가
산지마다 흙과 기후가 달라 '얼마나 마르면 가뭄인가'가 다릅니다. 각 산지의 평소를 기준으로 '평소보다 마른 날'을 세어 산지끼리 비교할 수 있게 했습니다. 관수 투자 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 평소보다 마른 날이 늘어나는 쪽입니다. 2001~2010년은 정의상 연평균 약 20%입니다.

## 주의점
- 기준 기간(2001~2010) 자체가 평년과 다를 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
