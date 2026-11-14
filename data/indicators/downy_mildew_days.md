---
id: downy_mildew_days
name: 노균병 감염 위험일
category: disease
order: 10
short: 생육 초기(4~6월) 동안 기온 10°C 이상에 비가 10mm 이상 온, 노균병이 처음 감염되기 쉬운 날 수
unit: 일
dataset: MERRA-2
source: NASA POWER 일별 T2M·PRECTOTCORR (MERRA-2 평균기온·강수)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육 초기 (4~6월, 남반구 10~12월)
condition: 일 평균기온 ≥ 10°C 그리고 일 강수량 ≥ 10mm  (3-10 규칙 단순형)
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [노균병, 곰팡이, 병해, 방제, 농약, 감염, 3-10, downy mildew]
---

## 정의
생육 초기(북반구 4~6월, 남반구 10~12월) 중 하루 평균기온이 10°C 이상이면서 비가 10mm 이상 온 날의 수입니다. 포도 노균병의 1차 감염 조건을 나타내는 '3-10 규칙'(새순 10cm, 기온 10°C, 비 10mm)을 날씨 부분만 단순하게 쓴 것입니다.

## 왜 중요한가
노균병은 잎과 송이를 말려 한 해 농사를 망칠 수 있는 대표 병입니다. 1차 감염 위험일이 늘면 첫 방제를 앞당기고 횟수를 늘려야 하므로, 방제 계획과 내병성 품종 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 노균병이 시작되기 좋은 날이 늘어나는 쪽입니다.

## 주의점
- 새순 길이 조건은 넣지 않았습니다. 실제 감염은 잎이 젖어 있는 시간에 크게 좌우됩니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
