---
id: water_balance
name: 생육기 물수지
category: drought
order: 10
short: 생육기 동안 내린 비에서 땅과 잎이 증발로 잃는 물을 뺀 값. 음수가 클수록 물이 모자람
unit: mm
dataset: MERRA-2
source: NASA POWER 일별 T2M·T2M_MAX·T2M_MIN·PRECTOTCORR (MERRA-2)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: Σ (강수량 − 기준 증발산량 ET0), ET0 는 Hargreaves 식 (FAO-56)
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: better
keywords: [물수지, 증발산, 가뭄, 물 부족, 관수, 관개, 건조 지수, ET0]
---

## 정의
생육기 동안 매일 (강수량 − 기준 증발산량)을 더한 값입니다. 기준 증발산량(ET0)은 기온과 위도로 계산하는 Hargreaves 식(FAO-56)을 썼습니다. 음수면 비보다 증발로 잃는 물이 많다는 뜻입니다.

## 왜 중요한가
강수량만 보면 기온이 올라 증발이 늘어나는 효과가 빠집니다. 물수지는 '실제로 얼마나 모자라는가'를 보여 주어 관수 시설 규모, 물 확보, 내건성 대목 판단에 가장 직접적입니다.

## 해석 가이드
- 기울기가 음수면 물 부족이 심해지는 쪽입니다.
- 와인 산지의 건조 지수(Riou)와 비슷한 생각이지만 토양 저장 물은 넣지 않은 단순형입니다.

## 주의점
- Hargreaves 식은 습한 곳에서 증발산을 크게, 바람 센 곳에서 작게 잡는 경향이 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
