---
id: rain_intensity_gs
name: 생육기 강수 강도
category: rain_water
order: 160
short: 생육기 동안 비가 온 날 하루 평균 강수량. 비가 얼마나 세차게 오는지
unit: "mm/일"
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: 비 온 날(≥1mm) 강수량 합 ÷ 비 온 날 수
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
keywords: [강수 강도, 세찬 비, 폭우, 토양 유실, 유거수]
---

## 정의
생육기 동안 비 온 날(1mm 이상)의 강수량을 모두 더해 비 온 날 수로 나눈 값입니다.

## 왜 중요한가
같은 양의 비라도 한꺼번에 세차게 오면 땅에 스며들지 못하고 흘러가 버려, 물은 부족하고 흙은 쓸려 갑니다. 피복작물·배수 관리 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 비가 더 세차게 오는 쪽입니다.

## 주의점
- MERRA-2 강수는 모델에 관측을 보정한 값이라 국지성 비를 작게 잡을 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
