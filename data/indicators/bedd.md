---
id: bedd
name: 유효 적산온도 (BEDD)
category: growth
order: 40
short: 적산온도와 비슷하지만 19°C를 넘는 더위는 더 쳐 주지 않는, 실제 숙성에 쓰이는 열의 합
unit: °C·일
dataset: MERRA-2
source: NASA POWER 일별 T2M (MERRA-2 2m 평균기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: Σ min(max(평균기온 − 10, 0), 9)  (단순형)
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: neutral
station_var: tmean
keywords: [적산온도, BEDD, 유효 적산온도, 숙성, 열, 품종, 당도]
---

## 정의
생육기 동안 매일 (평균기온 − 10°C)를 더하되, 하루에 9까지만 셉니다. 평균 19°C를 넘는 더위는 포도 숙성에 더 보태지 않는다는 생각을 담은 Gladstones의 지표를 단순하게 계산한 값입니다.

## 왜 중요한가
일반 적산온도는 더운 날을 많이 쳐 주어 더운 산지에서 숙성 속도를 부풀립니다. 이 지표와 일반 적산온도의 차이가 커지면 "더워졌지만 숙성에 도움이 안 되는 열"이 늘었다는 뜻이라, 품종 교체 판단을 보완합니다.

## 해석 가이드
- 일반 적산온도와 함께 보세요. 적산온도는 오르는데 BEDD가 덜 오르면 늘어난 열 대부분이 19°C를 넘는 더위입니다.

## 주의점
- 원래 Gladstones 지표의 위도·일교차 보정은 넣지 않은 단순형입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
- Gladstones, J. (1992), Viticulture and Environment. Winetitles
