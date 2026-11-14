---
id: thermal_gs_start
name: 생육 시작일 (기온 기준)
category: growth
order: 200
short: 평균기온 10°C 이상이 5일 이어진 첫날. 포도가 자라기 시작하는 기온상의 봄 (1월 1일부터, 남반구 7월 1일부터 센 날)
unit: "연중일"
dataset: MERRA-2
source: NASA POWER 일별 T2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 1~7월 (남반구 7~12월)
condition: 평균기온 ≥ 10°C 가 5일 이어진 첫날
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [생육 시작, 봄 시작, 발아, 기온, 앞당겨]
---

## 정의
1월 1일(남반구 7월 1일)부터 세어 하루 평균기온이 10°C 이상인 날이 처음으로 5일 연속된 날의 첫날입니다.

## 왜 중요한가
포도는 평균 10°C 근처부터 자라기 시작합니다. 이 날이 앞당겨지면 싹도 빨리 트고 늦서리 노출이 길어지므로 서리 대비와 품종 선택에 씁니다.

## 해석 가이드
- 기울기가 음수면 생육 시작이 앞당겨지는 쪽입니다. 위성 그린업 날짜와 비교해 보세요.

## 주의점
- 겨울에도 10°C를 자주 넘는 따뜻한 산지(바로사)는 의미가 약합니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
