---
id: spring_night_lst
name: 봄 밤 지표면 온도 (1km)
category: temp_frost
order: 170
short: 봄 서리 위험 시기에 MODIS 위성이 1km 해상도로 잰 밤 땅 표면 온도의 평균
unit: °C
dataset: MODIS
source: MODIS Aqua 야간 지표면 온도 (MYD11 LST_Night_1km), 8일 구간, 산지 영역 1km 픽셀 중앙값
start_year: 2003
resolution: 1km (산지 영역 약 11km 안 픽셀 중앙값)
stage: 봄 (서리 위험 구간)
stage_from: budburst
stage_to: flowering
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: better
keywords: [밤, 야간, 지표면 온도, 위성, 1km, 냉기, 서리 웅덩이, 골짜기, 봄 밤, MODIS, LST]
---

## 정의
봄 서리 위험 시기 동안 MODIS 위성(Aqua, 새벽 1시 30분 통과)이 1km 해상도로 잰 밤 땅 표면 온도를, 산지 영역 픽셀의 중앙값으로 평균한 값입니다.

## 왜 중요한가
50km 기후 격자로는 보이지 않는 밭 근처의 밤 추위를 위성으로 직접 봅니다. 같은 산지 안에서도 1km 픽셀끼리 밤 온도가 평균 3~6°C 차이 나서, 서리 대비 시설을 어디에 둘지 판단하는 보조 자료가 됩니다.

## 해석 가이드
- 기울기가 양수면 봄 밤이 따뜻해져 서리 위험이 줄어드는 쪽입니다.
- 땅 표면 온도는 2m 기온과 다른 물리량이라 절대값보다 변화 방향을 보세요.

## 주의점
- 구름 낀 밤은 값이 비어 있어 맑은 밤 위주로 평균됩니다(맑은 밤이 더 추움).
- 정확한 집계 기간(봄 구간의 시작·끝)은 MODIS 담당 작업 기준이며, 발표 전에 확인이 필요합니다.

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) 14_전전A_MODIS요약, 15_전전A_MODIS연도별
- Wan, Z. (2014), collection-6 MODIS LST — https://doi.org/10.1016/j.rse.2013.08.027
