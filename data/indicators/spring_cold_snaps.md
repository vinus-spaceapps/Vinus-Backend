---
id: spring_cold_snaps
name: 봄 급랭일
category: temp_frost
order: 50
short: 봄 동안 하루 평균기온이 전날보다 5°C 이상 뚝 떨어진 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 T2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 봄 (4/1~5/31, 남반구 10/1~11/30)
condition: 하루 평균기온이 전날보다 5°C 이상 떨어진 날
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
station_var: tmean
keywords: [급랭, 꽃샘추위, 봄 추위, 기온 급변, 날씨 변덕, 냉해]
---

## 정의
봄(4~5월, 남반구 10~11월) 중 하루 평균기온이 전날보다 5°C 이상 떨어진 날의 수입니다.

## 왜 중요한가
따뜻한 날씨에 새순이 빨리 자란 뒤 갑자기 추워지면 서리가 아니어도 새순이 상하고 꽃눈 분화가 흔들립니다. 서리 대비 시설과 보험 판단을 보완합니다.

## 해석 가이드
- 기울기가 양수면 봄 날씨의 급변이 잦아지는 쪽입니다.

## 주의점
- 50km 격자 평균이라 고도·경사면 차이는 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
