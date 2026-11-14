---
id: harvest_dry_spell
name: 수확기 최장 무강수 기간
category: drought
order: 90
short: 수확기(8~9월) 동안 비가 오지 않은 날이 가장 길게 이어진 일수
unit: "일"
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 수확기 (8~9월, 남반구 2~3월)
condition: 일 강수량 < 1mm 인 날이 가장 길게 이어진 기간
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: neutral
keywords: [맑은 수확기, 건조, 무강수, 수확 일정]
---

## 정의
수확기 동안 하루 강수량 1mm 미만인 날이 가장 길게 연속된 날 수입니다.

## 왜 중요한가
수확기의 긴 맑은 날은 송이가 마르고 건강하게 익게 해 품질에 좋지만, 너무 길면 포도알이 쪼그라들 수 있습니다. 수확 일정과 수확 직전 관수 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 수확기가 건조해지는 쪽입니다(대개 품질에 유리).

## 주의점
- 비가 거의 없는 산지(나파)는 늘 길게 나옵니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
