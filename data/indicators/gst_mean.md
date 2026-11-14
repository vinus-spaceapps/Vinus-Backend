---
id: gst_mean
name: 생육기 평균기온
category: growth
order: 20
short: 생육기 동안 하루 평균기온의 평균. 세계 와인 산지를 나누는 가장 기본적인 기후 지표
unit: °C
dataset: MERRA-2
source: NASA POWER 일별 T2M (MERRA-2 2m 평균기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 생육기 (4/1~10/31, 남반구 10/1~4/30)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [평균기온, 기온, 따뜻, 온난화, 기후대, 품종, 스타일, GST, 기온 상승]
---

## 정의
생육기(북반구 4월 1일~10월 31일, 남반구 10월 1일~4월 30일) 동안 하루 평균기온을 평균한 값입니다. 와인 기후 연구에서 산지를 나누는 기준(Growing Season Temperature)으로 가장 널리 씁니다.

## 왜 중요한가
어떤 스타일의 와인이 그 산지에서 나오는지를 가장 간단하게 보여 줍니다. 값이 오르면 지금 품종이 그 산지의 적정 범위를 벗어나는지 확인할 수 있어, 품종 교체 계획에 씁니다.

## 해석 가이드
- 기울기가 양수면 산지가 더 따뜻한 기후대로 옮겨 가는 중입니다.
- 구간(대략): 13~15°C 서늘함(리슬링·피노 누아), 15~17°C 중간(샤르도네·메를로), 17~19°C 따뜻함(카베르네 소비뇽·시라), 19~21°C 더움(그르나슈·진판델).

## 주의점
- 50km 격자 평균이라 고도·경사면 차이는 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
- Jones, G. V. et al. (2005), Climate change and global wine quality — https://doi.org/10.1007/s10584-005-4704-2
