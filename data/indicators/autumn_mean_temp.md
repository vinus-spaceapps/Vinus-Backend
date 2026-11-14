---
id: autumn_mean_temp
name: 가을 평균기온
category: growth
order: 180
short: 수확 뒤 가을(10~11월, 남반구 4~5월)의 하루 평균기온. 가지가 여무는 시기
unit: "°C"
dataset: MERRA-2
source: NASA POWER 일별 T2M
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 가을 (10~11월, 남반구 4~5월)
condition: (조건 없음) 기간 평균
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [가을, 목질화, 가지 여뭄, 월동 준비, 수확 후]
---

## 정의
수확이 끝난 가을 두 달(10~11월, 남반구 4~5월) 동안 하루 평균기온을 평균한 값입니다.

## 왜 중요한가
가을에 가지가 충분히 여물어야(목질화) 겨울 추위를 견딥니다. 가을이 너무 따뜻하면 여무는 시기가 늦어져 초겨울 한파에 약해지므로 월동 대책에 씁니다.

## 해석 가이드
- 기울기가 양수면 가을이 따뜻해지는 쪽입니다.

## 주의점
- 50km 격자 평균이라 고도·경사면 차이는 반영되지 않습니다.
- 팀 일별 원자료로 직접 계산한 지표입니다(scripts/import_team_xlsx.py 의 DERIVED).

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) D_ 일별 원자료에서 계산
- NASA POWER — https://power.larc.nasa.gov/
