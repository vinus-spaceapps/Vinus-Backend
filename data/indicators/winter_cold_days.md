---
id: winter_cold_days
name: 겨울 한파일수
category: temp_frost
order: 120
short: 겨울 동안 최저기온이 기준값(기본 −10°C) 이하로 내려간 날 수
unit: 일
dataset: MERRA-2
source: NASA POWER 일별 T2M_MIN (MERRA-2 2m 최저기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 겨울 (12~2월, 남반구 6~8월)
condition: 일 최저기온 ≤ 기준값
threshold: -10
threshold_unit: °C
threshold_options: [-5, -10, -15, -20]
aggregation: count
robust: false
higher_is: worse
station_var: tmin
keywords: [한파, 혹한, 겨울 동해, 얼어 죽, 겨울눈, 휴면, 강추위]
---

## 정의
겨울(북반구 전년 12월~2월, 남반구 6~8월) 중 하루 최저기온이 기준값 이하였던 날의 수입니다. 기본은 −10°C이고 −5·−15·−20°C로 바꿔 볼 수 있습니다.

## 왜 중요한가
겨울 최저기온이 '가장 추운 하루'라면, 이것은 '추운 날이 몇 번 왔나'입니다. 한파가 잦으면 겨울눈과 줄기 피해가 쌓이므로 흙덮기·바람막이 같은 월동 대책과 내한성 품종 판단에 씁니다.

## 해석 가이드
- 기울기가 음수면 한파가 줄어드는 쪽입니다.
- 포도나무 겨울눈은 대체로 −15~−20°C 아래에서 크게 상합니다.

## 주의점
- 오카나간은 격자가 관측소보다 약 5°C 춥게 나와 날 수가 크게 부풀 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
