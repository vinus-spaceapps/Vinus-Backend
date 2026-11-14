---
id: winter_warm_days
name: 겨울 이상 고온일
category: temp_frost
order: 150
short: 겨울 동안 최고기온이 기준값(기본 15°C) 이상으로 봄처럼 따뜻했던 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 T2M_MAX
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 겨울 (12~2월, 남반구 6~8월)
condition: 일 최고기온 ≥ 기준값
threshold: 15
threshold_unit: °C
threshold_options: [10, 15]
aggregation: count
robust: false
higher_is: worse
station_var: tmax
keywords: [겨울 이상 고온, 따뜻한 겨울날, 내한성, 겨울 해동, 동해]
---

## 정의
겨울 중 하루 최고기온이 기준값(기본 15°C) 이상이었던 날의 수입니다. 10°C로 바꿔 볼 수 있습니다.

## 왜 중요한가
한겨울에 며칠 따뜻하면 나무가 추위 대비(내한성)를 풀었다가 다시 오는 한파에 크게 상합니다. 따뜻한 날 뒤 한파가 잦은 산지의 월동 대책에 씁니다.

## 해석 가이드
- 기울기가 양수면 겨울 중 이상 고온이 잦아지는 쪽입니다. 겨울 한파일수와 함께 보세요.

## 주의점
- 50km 격자 평균이라 고도·경사면 차이는 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
