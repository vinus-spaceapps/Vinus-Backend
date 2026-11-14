---
id: winter_cold_sum
name: 겨울 추위 누적
category: temp_frost
order: 130
short: 겨울 동안 최저기온이 −10°C 아래로 내려간 만큼을 모두 더한 값. 한파의 총량
unit: "°C·일"
dataset: MERRA-2
source: NASA POWER 일별 T2M_MIN
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 겨울 (12~2월, 남반구 6~8월)
condition: Σ max(0, −10°C − 일 최저기온)
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: worse
station_var: tmin
keywords: [한파, 추위, 혹한, 누적, 동해, 겨울 피해]
---

## 정의
겨울 중 매일 −10°C보다 더 추웠던 만큼(예: −14°C면 4)을 모두 더한 값입니다.

## 왜 중요한가
한파일수가 '몇 번'이라면 이것은 '얼마나 깊고 길게'입니다. 겨울눈과 줄기 피해는 추위의 깊이와 지속에 비례하므로 내한성 품종·대목 판단에 씁니다.

## 해석 가이드
- 기울기가 음수면 한파의 총량이 줄어드는 쪽입니다.

## 주의점
- 오카나간은 격자 기온이 관측소보다 약 5°C 낮아 추위 지표가 부풀 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
