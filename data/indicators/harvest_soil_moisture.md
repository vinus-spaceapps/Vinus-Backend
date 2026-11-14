---
id: harvest_soil_moisture
name: 수확기 토양수분
category: drought
order: 130
short: 수확기(8~9월) 동안 뿌리층 흙의 습윤도 평균
unit: "0~1"
dataset: MERRA-2
source: NASA POWER 일별 GWETROOT
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 수확기 (8~9월, 남반구 2~3월)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
keywords: [수확기 토양, 땅속 물, 묽은 맛, 배수]
---

## 정의
수확기 동안 뿌리층 흙의 습윤도를 0~1 사이 값으로 평균한 것입니다.

## 왜 중요한가
익는 시기에 땅이 너무 젖으면 맛이 묽어지고 너무 마르면 숙성이 멈춥니다. 수확 전 관수 중단·배수 판단에 씁니다.

## 해석 가이드
- 산지마다 적정 값이 달라 절대값보다 변화 방향을 보세요.

## 주의점
- 모델 값입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
