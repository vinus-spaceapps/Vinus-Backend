---
id: harvest_rain_days
name: 수확기 비 일수
category: rain_water
short: 수확 전 3주 동안 하루 강수량이 기준값 이상이었던 날 수
unit: 일
dataset: GPM IMERG
source: GPM IMERG Final Run 일 강수 (GPM_3IMERGDF)
start_year: 2001
resolution: 약 10km
stage: 수확 전 3주
stage_from: harvest_minus_21
stage_to: harvest
condition: 일 강수량 ≥ 기준값
threshold: 10
threshold_unit: mm
threshold_options: [5, 10, 20]
aggregation: count
robust: false
higher_is: worse
keywords: [비, 강수, 장마, 습해, 곰팡이, 잿빛곰팡이, 열과, 터짐, 수확기 비, 태풍, rain]
---

## 정의
수확일 전 21일 동안 하루 강수량이 기준값(기본 10mm) 이상이었던 날의 수입니다.

## 왜 중요한가
수확 직전의 비는 포도알을 터지게 하고(열과) 잿빛곰팡이병을 퍼뜨려, 당도가 다 오르기 전에 서둘러 따게 만듭니다. 수확 계획, 비가림 시설 투자, 조생 품종 검토에 씁니다.

## 해석 가이드
- 기울기가 양수면 수확기에 비 오는 날이 잦아지는 쪽입니다.
- 비 일수는 0~10일 범위의 작은 정수라 해마다 크게 출렁입니다. 몇 해의 많은 비가 추세를 좌우하는지 함께 보세요.

## 주의점
- IMERG는 2014년 전후로 입력 위성 구성이 바뀌었습니다(TRMM→GPM). 그 시점 앞뒤의 차이는 자료 변화일 수 있습니다.
- 국지성 소나기는 10km 격자에서도 놓칠 수 있습니다.

## 근거
- Huffman et al., GPM IMERG Final Precipitation L3 1 day — https://doi.org/10.5067/GPM/IMERGDF/DAY/07
