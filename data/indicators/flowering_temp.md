---
id: flowering_temp
name: 개화기 평균기온
category: growth
order: 80
short: 꽃이 피는 달(6월, 남반구 12월)의 하루 평균기온. 열매가 잘 맺히는지(착과)에 영향
unit: °C
dataset: MERRA-2
source: NASA POWER 일별 T2M (MERRA-2 2m 평균기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 개화기 (6월, 남반구 12월)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [개화, 꽃, 착과, 꽃떨이, 결실, 송이, 수확량]
---

## 정의
포도꽃이 피는 달(북반구 6월, 남반구 12월)의 하루 평균기온을 평균한 값입니다.

## 왜 중요한가
꽃이 필 때 너무 춥거나(대략 15°C 아래) 너무 더우면 꽃가루받이가 잘 안 돼 열매가 덜 맺힙니다(꽃떨이). 그해 수확량을 가늠하고, 착과가 불안정한 품종을 피하는 데 씁니다.

## 해석 가이드
- 대략 20~25°C가 착과에 좋습니다. 이 범위에서 멀어지는지 보세요.

## 주의점
- 실제 개화 시기는 해마다·품종마다 달라 한 달 고정 기간은 근사입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
