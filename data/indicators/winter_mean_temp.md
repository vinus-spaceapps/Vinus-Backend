---
id: winter_mean_temp
name: 겨울 평균기온
category: temp_frost
order: 110
short: 겨울(12~2월, 남반구 6~8월)의 하루 평균기온
unit: "°C"
dataset: MERRA-2
source: NASA POWER 일별 T2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 겨울 (12~2월, 남반구 6~8월)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [겨울, 따뜻한 겨울, 휴면, 해충 월동, 겨울 기온]
---

## 정의
겨울 석 달 동안 하루 평균기온을 평균한 값입니다.

## 왜 중요한가
겨울이 따뜻해지면 혹한 피해는 줄지만 해충이 살아남고 휴면이 얕아져 봄 서리에 약해집니다. 월동 대책과 병해충 방제 계획에 씁니다.

## 해석 가이드
- 기울기가 양수면 겨울이 따뜻해지는 쪽입니다. 휴면기 저온 일수와 함께 보세요.

## 주의점
- 50km 격자 평균이라 고도·경사면 차이는 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
