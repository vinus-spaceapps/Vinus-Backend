---
id: powdery_mildew_days
name: 흰가루병 위험일
category: disease
order: 20
short: 생육기 동안 평균기온 21~30°C로 흰가루병 곰팡이가 가장 잘 자라는 날 수
unit: 일
dataset: MERRA-2
source: NASA POWER 일별 T2M·T2M_MAX (MERRA-2 평균·최고기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: 21°C ≤ 일 평균기온 ≤ 30°C 그리고 일 최고기온 < 35°C
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
station_var: tmean
keywords: [흰가루병, 곰팡이, 병해, 방제, 황, 농약, powdery mildew]
---

## 정의
생육기 동안 하루 평균기온이 21~30°C이고 최고기온이 35°C 미만이었던 날의 수입니다. 흰가루병 위험 지수(Gubler-Thomas)의 온도 조건을 하루 단위로 단순하게 쓴 것입니다.

## 왜 중요한가
흰가루병은 비가 없어도 따뜻하면 번지는 병이라, 건조한 산지에서도 방제 비용의 큰 몫을 차지합니다. 방제 간격을 정하고 내병성 품종을 고르는 데 씁니다.

## 해석 가이드
- 기울기가 양수면 흰가루병이 번지기 좋은 날이 늘어나는 쪽입니다. 35°C를 넘는 폭염은 오히려 곰팡이를 죽여 세지 않습니다.

## 주의점
- 원래 지수는 시간 단위(하루 중 6시간 이상)로 계산해 하루 평균은 근사입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
