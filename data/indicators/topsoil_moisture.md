---
id: topsoil_moisture
name: 생육기 겉흙 수분
category: drought
order: 110
short: 생육기 동안 겉흙(표층)이 얼마나 젖어 있는지(0=마름, 1=흠뻑)의 평균
unit: "0~1"
dataset: MERRA-2
source: NASA POWER 일별 GWETTOP
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: better
keywords: [겉흙, 표토, 토양수분, 가뭄, 피복]
---

## 정의
생육기 동안 겉흙(표층)의 습윤도를 0~1 사이 값으로 평균한 것입니다.

## 왜 중요한가
겉흙은 비에 빨리 반응해 짧은 가뭄을 먼저 보여 줍니다. 어린 나무와 얕은 뿌리 품종의 관수, 피복작물 관리 판단에 씁니다.

## 해석 가이드
- 기울기가 음수면 겉흙이 마르는 쪽입니다. 뿌리층 토양수분(깊은 흙)과 함께 보세요.

## 주의점
- 모델 값이며 관수한 밭의 실제 값과 다릅니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
