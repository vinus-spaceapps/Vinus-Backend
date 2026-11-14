---
id: gs_wind_mean
name: 생육기 평균 풍속
category: sun_wind
order: 70
short: 생육기 동안 지상 2m 하루 평균 풍속의 평균
unit: "m/s"
dataset: MERRA-2
source: NASA POWER 일별 WS2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
keywords: [바람, 풍속, 통풍, 방풍, 건조]
---

## 정의
생육기 동안 지상 2m 높이의 하루 평균 풍속을 평균한 값입니다.

## 왜 중요한가
적당한 바람은 잎을 말려 병을 줄이지만, 바람이 잦아지면 서리 위험이, 세지면 물 손실과 가지 꺾임이 늘어납니다. 방풍림·방상팬 판단에 씁니다.

## 해석 가이드
- 기울기가 음수면 바람이 약해지는 쪽입니다(복사 서리·병해 위험 증가).

## 주의점
- 50km 격자 평균이라 골짜기 바람길은 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
