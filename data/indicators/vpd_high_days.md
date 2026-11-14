---
id: vpd_high_days
name: 고VPD 일수
category: drought
order: 60
short: 생육기 동안 공기가 매우 메말라(VPD 1.5 kPa 이상) 잎이 물을 빼앗기는 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 T2M·RH2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: 증기압 부족(VPD) ≥ 1.5 kPa
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [VPD, 대기 건조, 물 스트레스, 증산, 기공]
---

## 정의
생육기 동안 하루 평균 증기압 부족(VPD)이 1.5 kPa 이상이었던 날의 수입니다.

## 왜 중요한가
VPD가 높은 날에는 흙에 물이 있어도 포도나무가 기공을 닫아 광합성이 멈춥니다. 미세살수·차광과 관수 시점 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 대기 건조 스트레스가 잦아지는 쪽입니다.

## 주의점
- 하루 평균값으로 계산한 근사입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
