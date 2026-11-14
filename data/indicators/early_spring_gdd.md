---
id: early_spring_gdd
name: 이른 봄 적산온도
category: growth
order: 60
short: 이른 봄(1~3월) 동안 평균기온이 5°C를 넘은 만큼의 합. 싹을 일찍 깨우는 온기
unit: "°C·일"
dataset: MERRA-2
source: NASA POWER 일별 T2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 이른 봄 (1~3월, 남반구 7~9월)
condition: Σ max(0, 평균기온 − 5°C)
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: worse
station_var: tmean
keywords: [이른 봄, 발아 촉진, 따뜻한 봄, 조기 발아, 늦서리]
---

## 정의
이른 봄(1~3월, 남반구 7~9월) 동안 매일 평균기온이 5°C를 넘은 만큼을 모두 더한 값입니다.

## 왜 중요한가
이른 봄이 따뜻하면 싹이 빨리 트고, 그 뒤 늦서리를 맞을 위험이 커집니다. 싹트는 날짜·서리 지표와 함께 서리 대비 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 싹이 더 일찍 깨는 쪽입니다(서리 노출 증가).

## 주의점
- 50km 격자 평균이라 고도·경사면 차이는 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
