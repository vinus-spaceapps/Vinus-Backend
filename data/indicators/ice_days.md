---
id: ice_days
name: 겨울 결빙일수
category: temp_frost
order: 140
short: 겨울 동안 낮에도 영하(최고기온 0°C 이하)였던 날 수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 T2M_MAX
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 겨울 (12~2월, 남반구 6~8월)
condition: 일 최고기온 ≤ 0°C
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
station_var: tmax
keywords: [결빙, 영하, 꽁꽁, 땅 얼음, 동결, 한파]
---

## 정의
겨울 중 하루 최고기온이 0°C 이하, 즉 하루 종일 얼어 있던 날의 수입니다.

## 왜 중요한가
하루 종일 영하인 날이 이어지면 땅이 깊이 얼고 뿌리와 줄기 아래쪽이 상할 수 있습니다. 흙덮기·뿌리 보호 같은 월동 대책 판단에 씁니다.

## 해석 가이드
- 기울기가 음수면 하루 종일 언 날이 줄어드는 쪽입니다.

## 주의점
- 오카나간은 격자 기온이 관측소보다 약 5°C 낮아 추위 지표가 부풀 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
