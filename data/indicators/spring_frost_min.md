---
id: spring_frost_min
name: 봄 최저기온
category: temp_frost
order: 30
short: 싹이 트는 봄(4~5월, 남반구 10~11월) 중 가장 추웠던 날의 최저기온. 서리의 세기
unit: °C
dataset: MERRA-2
source: NASA POWER 일별 T2M_MIN (MERRA-2 2m 최저기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 봄 (4/1~5/31, 남반구 10/1~11/30)
condition: (조건 없음) 기간 중 최솟값
threshold:
threshold_unit:
threshold_options: []
aggregation: min
robust: false
higher_is: better
station_var: tmin
keywords: [봄 서리, 늦서리, 서리 강도, 냉해, 영하, 새순, 얼어, 가장 추운]
---

## 정의
봄(북반구 4월 1일~5월 31일, 남반구 10월 1일~11월 30일) 중 하루 최저기온이 가장 낮았던 값입니다. 서리일수가 "몇 번"이라면 이것은 "얼마나 세게"입니다.

## 왜 중요한가
새순은 −2°C 아래에서 크게 상합니다. 서리 날 수는 같아도 가장 추운 밤이 더 차가워지면 피해가 커지므로, 방상팬·살수 같은 시설의 필요성을 판단할 때 씁니다.

## 해석 가이드
- 기울기가 양수면 봄의 가장 추운 밤이 덜 추워지는 쪽입니다.
- 싹튼 뒤 서리일수와 함께 보세요.

## 주의점
- 골짜기 바닥의 냉기는 50km 격자에서 잘 잡히지 않아 실제 밭은 더 추울 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
