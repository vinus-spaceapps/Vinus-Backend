---
id: frost_after_budburst
name: 싹튼 뒤 서리일수
category: temp_frost
short: 싹이 튼 뒤 개화 전까지 최저기온이 기준값 아래로 떨어진 날 수
unit: 일
dataset: MERRA-2
source: MERRA-2 M2SDNXSLV T2MMIN (2m 일 최저기온)
start_year: 1981
resolution: 약 50km
stage: 발아~개화
stage_from: budburst
stage_to: flowering
condition: 일 최저기온 < 기준값
threshold: 0
threshold_unit: °C
threshold_options: [0, -1, -2]
aggregation: count
robust: false
higher_is: worse
keywords: [서리, 냉해, 봄서리, 늦서리, 발아, 싹, 새순, 영하, 얼어, 동해, 서리 피해, frost]
---

## 정의
싹이 튼 날부터 꽃이 피기 전까지, 하루 최저기온이 기준값(기본 0°C)보다 낮았던 날의 수입니다. 해마다 하나의 숫자로 셉니다.

## 왜 중요한가
싹이 튼 뒤의 새순은 영하에 쉽게 얼어 그해 수확량을 크게 줄입니다. 방상팬·살수 같은 서리 대비 시설 투자나 서리 보험 가입을 고민할 때 "우리 산지에서 이런 날이 늘고 있는가"를 확인하는 데 씁니다.

## 해석 가이드
- 기울기가 양수면 싹튼 뒤 서리 위험이 커지는 쪽, 음수면 줄어드는 쪽입니다.
- 온난화로 서리 자체는 줄어도 발아가 더 빨라지면 "싹튼 뒤" 서리는 줄지 않을 수 있습니다. 생육 단계 날짜를 우리 밭 기록으로 넣으면 더 정확합니다.
- 서리 피해는 몇몇 해에 몰려 나오므로, 추세가 유의하지 않아도 극단값 연도를 함께 보세요.

## 주의점
- MERRA-2는 약 50km 격자라 골짜기 바닥의 냉기 호수(cold air pooling)는 잘 잡지 못합니다. 실제 밭은 더 추울 수 있습니다.
- 2m 기온이므로 새순 높이의 온도와 다를 수 있습니다.

## 근거
- 2024년 남호주 서리 손실 20억 호주달러 이상 추정 — 기획서 v2 문제 정의 표
- Gelaro et al. (2017), The Modern-Era Retrospective Analysis for Research and Applications, Version 2 (MERRA-2) — https://doi.org/10.1175/JCLI-D-16-0758.1
