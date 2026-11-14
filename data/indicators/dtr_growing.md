---
id: dtr_growing
name: 생육기 일교차
category: growth
order: 170
short: 생육기 동안 하루 최고기온과 최저기온 차이의 평균
unit: °C
dataset: MERRA-2
source: NASA POWER 일별 T2M_MAX·T2M_MIN (MERRA-2 2m 최고·최저기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: (조건 없음) (최고기온 − 최저기온) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: better
station_var: tmean
keywords: [일교차, 낮밤, 밤 기온, 향, 색, 산도, 안토시아닌]
---

## 정의
생육기 동안 매일 (최고기온 − 최저기온)을 구해 평균한 값입니다.

## 왜 중요한가
낮에 따뜻하고 밤에 서늘하면(일교차가 크면) 포도가 색과 향, 산도를 잘 지킵니다. 일교차가 줄면 같은 평균기온이라도 품질이 떨어질 수 있어 품종·밭 선택에 참고합니다.

## 해석 가이드
- 기울기가 음수면 밤이 낮보다 더 빨리 더워지고 있다는 뜻입니다.

## 주의점
- 50km 격자라 골짜기·산비탈의 일교차보다 작게 나옵니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
