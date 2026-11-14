---
id: cool_night_index
name: 서늘한 밤 지수
category: growth
order: 110
short: 수확 직전 달(9월, 남반구 3월)의 하루 최저기온 평균
unit: °C
dataset: MERRA-2
source: NASA POWER 일별 T2M_MIN (MERRA-2 2m 최저기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 9월 (남반구 3월)
stage_from: veraison
stage_to: harvest
condition: (조건 없음) 월 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
station_var: tmin
keywords: [밤, 야간, 열대야, 밤 기온, 일교차, 산도, 향, 색, 착색, 서늘한 밤, cool night]
---

## 정의
포도가 익는 마지막 달(북반구 9월, 남반구 3월)의 하루 최저기온을 평균한 값입니다. 와인 기후 분류에서 쓰는 Cool Night Index와 같습니다.

## 왜 중요한가
익어 가는 시기의 밤이 서늘해야 포도가 향과 산도, 색을 지킵니다. 밤이 더워지면 산도가 빨리 떨어지고 향이 약해집니다. 품종 교체, 수확 시기 조정, 고지대 밭 확보를 고민할 때 씁니다.

## 해석 가이드
- 기울기가 양수면 익는 시기의 밤이 더워지는 쪽입니다.
- 구간: 12°C 이하 매우 서늘한 밤, 12~14°C 서늘한 밤, 14~18°C 온화한 밤, 18°C 초과 따뜻한 밤.

## 주의점
- 한 달 평균이라 그해 수확이 9월보다 일찍 끝났다면 실제 익는 시기와 어긋날 수 있습니다.

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) 2_와인지표_데이터, 7_연도별지표
- Tonietto & Carbonneau (2004) — https://doi.org/10.1016/j.agrformet.2003.06.001
