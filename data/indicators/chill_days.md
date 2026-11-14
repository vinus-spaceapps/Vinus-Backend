---
id: chill_days
name: 휴면기 저온 일수
category: temp_frost
order: 160
short: 휴면기(11~3월, 남반구 5~9월) 동안 평균기온이 0~7.2°C인, 겨울잠을 깨우는 데 필요한 서늘한 날 수
unit: 일
dataset: MERRA-2
source: NASA POWER 일별 T2M (MERRA-2 2m 평균기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 휴면기 (11~3월, 남반구 5~9월)
condition: 0°C < 일 평균기온 ≤ 7.2°C
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: better
station_var: tmean
keywords: [저온 요구, 휴면, 겨울잠, 발아 불량, 따뜻한 겨울, 저온 충족, chilling]
---

## 정의
휴면기 동안 하루 평균기온이 0°C 초과 7.2°C 이하였던 날의 수입니다. 과수 연구에서 쓰는 '저온 시간'을 하루 단위로 단순하게 센 값입니다.

## 왜 중요한가
포도나무는 겨울에 일정 기간 서늘해야 봄에 고르게 싹이 틉니다. 겨울이 너무 따뜻하면 싹이 들쭉날쭉 트고 수확량이 줄 수 있어, 따뜻한 산지의 품종·관리 판단에 씁니다.

## 해석 가이드
- 기울기가 음수면 겨울이 따뜻해져 저온이 부족해지는 쪽입니다.
- 포도는 다른 과수보다 저온 요구가 적은 편이라, 바로사·나파처럼 따뜻한 산지에서 의미가 큽니다.

## 주의점
- 원래는 시간 단위로 세는 지표라 하루 평균으로는 근사입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
