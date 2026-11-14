---
id: spring_mean_temp
name: 봄 평균기온
category: growth
order: 70
short: 봄 석 달(3~5월, 남반구 9~11월)의 하루 평균기온. 싹트는 시기를 정하는 기온
unit: °C
dataset: MERRA-2
source: NASA POWER 일별 T2M (MERRA-2 2m 평균기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 봄 (3~5월, 남반구 9~11월)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [봄, 봄 기온, 발아 시기, 싹, 빨라진 봄, 이른 봄]
---

## 정의
봄 석 달(북반구 3~5월, 남반구 9~11월) 동안 하루 평균기온을 평균한 값입니다.

## 왜 중요한가
봄이 따뜻할수록 싹이 일찍 틉니다. 봄은 빨리 따뜻해지는데 늦서리는 그대로라면 서리 피해가 커지므로, 싹트는 날짜·서리 지표와 함께 서리 대비 판단에 씁니다.

## 해석 가이드
- 기울기가 양수면 봄이 따뜻해져 싹이 빨리 트는 쪽입니다. 싹트는 날짜(그린업)와 같은 방향인지 보세요.

## 주의점
- 50km 격자 평균입니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
