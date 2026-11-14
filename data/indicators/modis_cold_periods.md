---
id: modis_cold_periods
name: 1km 냉기 구간 수
category: temp_frost
order: 60
short: 봄 서리 시기에 산지 안 가장 추운 1km 땅이 영하였던 8일 구간의 수 (위성으로 찾은 서리 웅덩이)
unit: "구간"
dataset: MODIS
source: MODIS Aqua 야간 지표면 온도 (8일 구간, 산지 영역 1km 픽셀 중 가장 추운 값)
start_year: 2001
resolution: 1km (산지 영역 약 11km 안 픽셀)
stage: 봄 (서리 위험 구간)
condition: 가장 추운 1km 픽셀의 밤 지표면 온도 ≤ 0°C 인 8일 구간 수
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [서리 웅덩이, 냉기, 골짜기, 1km, 위성, 저지대, MODIS]
---

## 정의
봄 서리 위험 시기 동안, 산지 영역의 1km 픽셀 가운데 가장 추운 곳의 밤 지표면 온도가 0°C 이하였던 8일 구간의 수입니다.

## 왜 중요한가
50km 기후 격자 평균으로는 영상이어도, 골짜기 바닥 같은 일부 땅은 영하로 떨어집니다. 서리 웅덩이가 얼마나 자주 생기는지 보여 주어 방상팬을 어디에 둘지, 저지대 밭을 피할지 판단하는 데 씁니다.

## 해석 가이드
- 기울기가 음수면 서리 웅덩이가 생기는 일이 줄어드는 쪽입니다.

## 주의점
- 구름 낀 구간은 비어 있어 실제보다 적게 셀 수 있습니다.
- 정확한 집계 기간은 MODIS 담당 작업 기준이며 확인이 필요합니다.

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) 14_전전A_MODIS요약, 15_전전A_MODIS연도별
