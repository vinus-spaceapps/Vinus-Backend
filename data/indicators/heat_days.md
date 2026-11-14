---
id: heat_days
name: 생육기 폭염일수
category: heat
order: 10
short: 생육기(4~10월, 남반구 10~4월) 동안 최고기온이 기준값 이상이었던 날 수
unit: 일
dataset: MERRA-2
source: NASA POWER 일별 T2M_MAX (MERRA-2 2m 최고기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
stage_from: budburst
stage_to: harvest
condition: 일 최고기온 ≥ 기준값
threshold: 35
threshold_unit: °C
threshold_options: [30, 32, 35, 38]
aggregation: count
robust: false
higher_is: worse
station_var: tmax
keywords: [폭염, 더위, 고온, 열, 일소, 햇볕 데임, 뜨거, 무더위, heat]
---

## 정의
생육기(북반구 4월 1일~10월 31일, 남반구 10월 1일~4월 30일) 동안 하루 최고기온이 기준값 이상이었던 날의 수입니다. 기본은 35°C(폭염)이고 30°C(고온)·32°C·38°C로 바꿔 볼 수 있습니다.

## 왜 중요한가
35°C를 넘는 날이 이어지면 광합성이 멈추고 포도알이 햇볕에 데이며(일소), 산도가 빠르게 떨어집니다. 내열성 품종으로의 교체, 차광망·관수 투자, 수확 시기 조정을 고민할 때 씁니다.

## 해석 가이드
- 기울기가 양수면 고온 스트레스가 늘어나는 쪽입니다.
- 서늘한 산지(모젤·부르고뉴)는 35°C 날이 거의 없어 0인 해가 많습니다. 이런 곳은 기준을 30°C로 바꿔 보세요.

## 주의점
- 50km 격자 평균이라 경사면 방향·고도 차이는 반영되지 않습니다.
- 근처 관측소와 비교한 최고기온 오차가 산지마다 다릅니다(바로사 약 +2°C, 오카나간 약 −5°C).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) 2_와인지표_데이터, 7_연도별지표
- NASA POWER — https://power.larc.nasa.gov/
