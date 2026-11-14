---
id: harvest_rain_days
name: 수확기 호우일수
category: rain_water
order: 20
short: 수확기(8~9월, 남반구 2~3월) 하루 강수량이 기준값 이상이었던 날 수
unit: 일
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR (MERRA-2 관측 보정 강수)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 수확기 (8~9월, 남반구 2~3월)
stage_from: veraison
stage_to: harvest
condition: 일 강수량 ≥ 기준값
threshold: 20
threshold_unit: mm
threshold_options: [10, 20, 30]
aggregation: count
robust: false
higher_is: worse
keywords: [비, 강수, 호우, 장마, 습해, 곰팡이, 잿빛곰팡이, 열과, 터짐, 수확기 비, 태풍, rain]
---

## 정의
수확기(북반구 8~9월, 남반구 2~3월) 동안 하루 강수량이 기준값(기본 20mm) 이상이었던 날의 수입니다. 10mm·30mm로 바꿔 볼 수 있습니다.

## 왜 중요한가
수확 직전의 큰비는 포도알을 터지게 하고(열과) 잿빛곰팡이병을 퍼뜨려, 당도가 다 오르기 전에 서둘러 따게 만듭니다. 수확 계획, 비가림 시설 투자, 조생 품종 검토에 씁니다.

## 해석 가이드
- 기울기가 양수면 수확기에 큰비가 잦아지는 쪽입니다.
- 0~10일 범위의 작은 정수라 해마다 크게 출렁입니다. 비가 적은 산지(나파·오카나간)는 거의 늘 0입니다. 수확기 강수량을 함께 보세요.

## 주의점
- MERRA-2 강수는 모델에 관측을 보정한 값이라 국지성 호우를 작게 잡을 수 있습니다. GPM IMERG(약 10km)로 교차 확인할 계획입니다.

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) 2_와인지표_데이터, 7_연도별지표
- NASA POWER — https://power.larc.nasa.gov/
