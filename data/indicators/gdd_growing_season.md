---
id: gdd_growing_season
name: 생육기 적산온도
category: growth
order: 10
short: 생육기(4~10월, 남반구 10~4월) 하루 평균기온이 10°C를 넘은 만큼을 모두 더한 값
unit: °C·일
dataset: MERRA-2
source: NASA POWER 일별 T2M (MERRA-2 2m 평균기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
stage_from: budburst
stage_to: harvest
condition: 일 평균기온 − 10°C (0 미만은 0)
threshold: 10
threshold_unit: °C
threshold_options: [10]
aggregation: sum
robust: false
higher_is: neutral
station_var: tmean
keywords: [적산온도, 온도 합, 생육도일, 따뜻, 기온 상승, 온난화, 품종, 숙기, 당도, GDD, winkler]
---

## 정의
생육기(북반구 4월 1일~10월 31일, 남반구 10월 1일~4월 30일) 동안 하루 평균기온이 10°C를 넘은 만큼(예: 평균 18°C인 날은 8)을 모두 더한 값입니다. 포도 재배에서 쓰는 윙클러 지수와 같은 방식입니다.

## 왜 중요한가
적산온도는 어떤 품종이 그 산지에서 잘 익는지를 정하는 가장 기본적인 기준입니다. 값이 꾸준히 오르면 지금 품종이 너무 빨리 익어 산도가 부족해질 수 있어, 재식재(품종 교체) 계획에 씁니다.

## 해석 가이드
- 기울기가 양수면 산지가 더 따뜻한 기후대 쪽으로 옮겨 가는 중입니다. 윙클러 구역 경계(1390, 1670, 1940, 2220 °C·일)를 넘는지 보세요.
- 좋고 나쁨은 품종에 따라 다릅니다. 서늘한 산지에서는 도움이 되기도 합니다.

## 주의점
- 생육 기간을 날짜로 고정해 실제 발아·수확이 앞당겨진 효과는 빠집니다.
- 근처 관측소와 비교하면 나파는 격자 적산온도가 관측보다 조금 높게 나옵니다(4~9월 비교).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) 2_와인지표_데이터, 7_연도별지표, 12_전전C_관측소적산온도
- Jones et al. (2010), climate in winegrape growing regions — https://doi.org/10.5344/ajev.2010.61.3.313
