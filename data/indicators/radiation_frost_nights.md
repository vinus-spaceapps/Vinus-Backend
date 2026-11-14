---
id: radiation_frost_nights
name: 복사 서리 위험 밤
category: temp_frost
order: 40
short: 봄 동안 바람이 약하고(2 m/s 미만) 최저기온이 2°C 이하로 내려간, 땅이 식어 서리가 잘 앉는 밤 수
unit: 일
dataset: MERRA-2
source: NASA POWER 일별 T2M_MIN·WS2M (MERRA-2 2m 최저기온·풍속)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 봄 (4/1~5/31, 남반구 10/1~11/30)
condition: 일 최저기온 ≤ 2°C 그리고 일평균 풍속 < 2 m/s
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
station_var: tmin
keywords: [복사 서리, 바람 없는 밤, 맑은 밤, 냉기, 방상팬, 서리 위험, 고요한]
---

## 정의
봄(북반구 4~5월, 남반구 10~11월) 중 하루 최저기온이 2°C 이하이면서 하루 평균 풍속이 2 m/s 미만이었던 날의 수입니다.

## 왜 중요한가
바람 없는 맑은 밤에는 땅의 열이 하늘로 빠져나가 골짜기 바닥에 찬 공기가 고이고 서리가 앉습니다(복사 서리). 방상팬은 이런 밤에 위의 따뜻한 공기를 섞어 서리를 막으므로, 방상팬 투자 판단에 가장 직접적인 지표입니다.

## 해석 가이드
- 기울기가 양수면 방상팬이 필요한 밤이 늘어나는 쪽입니다.
- 격자 최저기온이 2°C여도 골짜기 바닥은 영하일 수 있어 기준을 2°C로 잡았습니다.

## 주의점
- 일평균 풍속이라 밤사이 바람이 잦아든 경우를 놓칠 수 있습니다.
- 산지마다 평소 바람 세기가 달라 산지끼리 날 수를 그대로 비교하기는 어렵습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
