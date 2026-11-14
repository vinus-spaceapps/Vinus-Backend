---
id: vpd_mean
name: 생육기 증기압 부족 (VPD)
category: drought
order: 50
short: 생육기 공기가 얼마나 메말라 잎에서 물을 빨아들이는지의 평균 (클수록 건조 스트레스)
unit: kPa
dataset: MERRA-2
source: NASA POWER 일별 T2M·RH2M (MERRA-2 평균기온·상대습도)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: 포화 수증기압(평균기온) × (1 − 상대습도/100) 의 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
keywords: [VPD, 증기압 부족, 건조, 대기 건조, 물 스트레스, 증산, 잎 마름]
---

## 정의
생육기 동안 매일 '그 온도에서 공기가 머금을 수 있는 수증기'와 '실제 수증기'의 차이(kPa)를 구해 평균한 값입니다. 클수록 공기가 메말라 잎에서 물이 빨리 빠져나갑니다.

## 왜 중요한가
흙에 물이 있어도 공기가 너무 메마르면 포도나무가 기공을 닫아 광합성과 당 축적이 멈춥니다. 관수 시점, 차광·미세살수 투자, 내건성 품종 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 공기가 더 메말라지는 쪽입니다. 대략 1.5 kPa를 넘는 날이 많으면 물 스트레스가 큽니다.

## 주의점
- 일평균 기온·습도로 계산해 한낮의 실제 VPD보다 작게 나옵니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
