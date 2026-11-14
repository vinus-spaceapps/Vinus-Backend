---
id: winter_rain
name: 휴면기 강수량
category: rain_water
order: 180
short: 휴면기(11~3월, 남반구 5~9월)에 내린 비의 총량. 봄에 쓸 땅속 물을 채우는 비
unit: mm
dataset: MERRA-2
source: NASA POWER 일별 PRECTOTCORR (MERRA-2 관측 보정 강수)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 휴면기 (11~3월, 남반구 5~9월)
condition: (조건 없음) 기간 합계
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: better
keywords: [겨울 비, 겨울 강수, 땅속 물, 저수, 가뭄, 관수, 토양 수분 보충]
---

## 정의
휴면기(북반구 전년 11월~3월, 남반구 5~9월)에 내린 비를 모두 더한 양입니다.

## 왜 중요한가
여름이 건조한 산지(나파·바로사·보르도)는 겨울비로 채운 땅속 물로 한 해를 버팁니다. 겨울비가 줄면 봄부터 관수가 필요해지므로 관수 시설·물 확보 판단에 씁니다.

## 해석 가이드
- 기울기가 음수면 땅속 물이 덜 채워지는 쪽입니다. 생육기 물수지와 함께 보세요.

## 주의점
- 눈으로 내린 양도 물로 환산되어 포함됩니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
