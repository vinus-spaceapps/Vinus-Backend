---
id: ripening_temp
name: 수확기 평균기온
category: growth
order: 120
short: 포도가 익는 마지막 두 달(8~9월, 남반구 2~3월)의 하루 평균기온
unit: °C
dataset: MERRA-2
source: NASA POWER 일별 T2M (MERRA-2 2m 평균기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 수확기 (8~9월, 남반구 2~3월)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
station_var: tmean
keywords: [수확기, 숙성기, 익는 시기, 기온, 산도, 향, 당도, 알코올]
---

## 정의
수확기(북반구 8~9월, 남반구 2~3월) 동안 하루 평균기온을 평균한 값입니다.

## 왜 중요한가
익는 시기가 더우면 당은 빨리 오르지만 산도와 향이 빠져, 알코올만 높고 밋밋한 와인이 되기 쉽습니다. 수확 시기를 앞당길지, 그늘·관수를 늘릴지 판단할 때 씁니다.

## 해석 가이드
- 기울기가 양수면 익는 시기가 더워지는 쪽입니다. 서늘한 밤 지수(밤 기온)와 함께 보세요.

## 주의점
- 수확이 이 기간보다 일찍 끝나는 해에는 실제 익는 시기와 어긋날 수 있습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
