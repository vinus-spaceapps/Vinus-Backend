---
id: ripening_dtr
name: 수확기 일교차
category: growth
order: 160
short: 포도가 익는 마지막 두 달(8~9월, 남반구 2~3월) 하루 최고·최저기온 차이의 평균
unit: °C
dataset: MERRA-2
source: NASA POWER 일별 T2M_MAX·T2M_MIN (MERRA-2 2m 최고·최저기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 수확기 (8~9월, 남반구 2~3월)
condition: (조건 없음) (최고기온 − 최저기온) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: better
station_var: tmean
keywords: [일교차, 수확기, 숙성기, 색, 향, 산도, 안토시아닌, 낮밤]
---

## 정의
수확기(북반구 8~9월, 남반구 2~3월) 동안 매일 (최고기온 − 최저기온)을 구해 평균한 값입니다.

## 왜 중요한가
익는 시기의 큰 일교차는 레드 와인의 색(안토시아닌)과 향, 산도를 지켜 줍니다. 생육기 전체 일교차보다 품질에 더 직접적이라 품종·밭 선택과 수확 시기 판단에 씁니다.

## 해석 가이드
- 기울기가 음수면 익는 시기의 밤이 상대적으로 더워지는 쪽입니다. 서늘한 밤 지수와 함께 보세요.

## 주의점
- 50km 격자라 골짜기·산비탈의 일교차보다 작게 나옵니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
