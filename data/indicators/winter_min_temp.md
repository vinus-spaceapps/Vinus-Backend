---
id: winter_min_temp
name: 겨울 최저기온
category: temp_frost
order: 100
short: 겨울(12~2월, 남반구 6~8월) 동안 가장 추웠던 날의 최저기온
unit: °C
dataset: MERRA-2
source: NASA POWER 일별 T2M_MIN (MERRA-2 2m 최저기온)
start_year: 2002
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 겨울 (12~2월, 남반구 6~8월)
stage_from: harvest
stage_to: budburst
condition: (조건 없음) 기간 중 최솟값
threshold:
threshold_unit:
threshold_options: []
aggregation: min
robust: false
higher_is: better
station_var: tmin
keywords: [겨울, 동해, 혹한, 한파, 얼어 죽, 나무가 죽, 겨울 냉해, 휴면, 눈, winter, cold]
---

## 정의
그해 겨울(북반구는 전년 12월~2월, 남반구는 6~8월) 하루 최저기온 가운데 가장 낮은 값입니다. 해마다 "그 겨울에 가장 추웠던 순간"을 하나의 숫자로 봅니다.

## 왜 중요한가
포도나무는 휴면 중이라도 영하 15~20°C 아래로 떨어지면 눈(겨울눈)과 줄기가 얼어 죽습니다. 2024년 1월 캐나다 오카나간 한파로 이듬해 수확 대부분을 잃었습니다. 내한성 품종·대목 선택, 흙덮기 같은 월동 대책 투자를 고민할 때 씁니다.

## 해석 가이드
- 기울기가 양수면 겨울 최저기온이 올라 혹한 위험이 줄어드는 쪽입니다.
- 평균이 따뜻해져도 한 해의 극단적인 한파는 여전히 올 수 있습니다. 극단값 연도를 함께 보세요.

## 주의점
- 첫 시즌(2001년)은 전년 12월 자료가 없어 2002년부터 계산합니다.
- 오카나간은 격자 최저기온이 근처 관측소보다 약 5°C 낮게 나옵니다. 절대값보다 변화 방향을 보세요.

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) 3_산지좌표(오카나간 2024 겨울 동해), 7_연도별지표
- NASA POWER — https://power.larc.nasa.gov/
