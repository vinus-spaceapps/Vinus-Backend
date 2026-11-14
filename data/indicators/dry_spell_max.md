---
id: dry_spell_max
name: 생육기 최장 무강수 기간
category: drought
order: 80
short: 생육기 동안 비(1mm 이상)가 오지 않은 날이 가장 길게 이어진 일수
unit: 일
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR (MERRA-2 관측 보정 강수)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: 일 강수량 < 1mm 인 날이 가장 길게 이어진 기간
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [가뭄, 건조, 마른 장마, 비가 안 와, 물 부족, 관수, 관개, 연속]
---

## 정의
생육기 동안 하루 강수량이 1mm 미만인 날이 가장 길게 연속된 날 수입니다.

## 왜 중요한가
강수량 합계가 같아도 비가 한동안 끊기면 포도나무가 심한 물 스트레스를 받습니다. 관수 시설의 필요성, 대목·품종의 내건성 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 마른 기간이 길어지는 쪽입니다. 뿌리층 토양수분과 함께 보세요.

## 주의점
- 비가 거의 오지 않는 여름(나파·바로사)은 늘 길게 나와 변화가 잘 드러나지 않을 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
