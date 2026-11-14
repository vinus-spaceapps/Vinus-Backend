---
id: last_spring_frost
name: 마지막 봄 서리 날
category: temp_frost
order: 70
short: 그해 봄 마지막으로 서리(최저기온 0°C 이하)가 내린 날짜 (1월 1일부터 센 날, 남반구는 7월 1일부터)
unit: 연중일
dataset: MERRA-2
source: NASA POWER 일별 T2M_MIN (MERRA-2 2m 최저기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 1~6월 (남반구 7~12월)
condition: 일 최저기온 ≤ 기준값 인 마지막 날
threshold: 0
threshold_unit: °C
threshold_options: [0, -2]
aggregation: mean
robust: false
higher_is: worse
station_var: tmin
keywords: [늦서리, 마지막 서리, 봄 서리, 서리 날짜, 발아, 싹, 언제까지]
---

## 정의
1~6월(남반구 7~12월) 중 하루 최저기온이 기준값 이하였던 마지막 날을, 1월 1일을 1로 세어 나타낸 값입니다(남반구는 7월 1일을 1로 셈). 예: 100 = 4월 10일 무렵.

## 왜 중요한가
마지막 서리가 싹트는 날짜보다 늦으면 새순이 얼 위험이 있습니다. 싹트는 날짜(그린업)와 함께 보면 "서리는 빨리 끝나는데 싹은 더 빨리 트는지"를 확인할 수 있어, 서리 대비 투자에 씁니다.

## 해석 가이드
- 기울기가 음수면 마지막 서리가 앞당겨지는 쪽입니다. 싹트는 날짜가 더 빨리 앞당겨지면 서리 위험은 오히려 커집니다.

## 주의점
- 서리가 없는 해는 값이 비어 있습니다. 서리가 드문 산지(바로사)는 분석할 연도가 부족할 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
