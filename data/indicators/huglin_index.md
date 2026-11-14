---
id: huglin_index
name: Huglin 지수
category: growth
order: 30
short: 어떤 포도 품종이 익을 수 있는지 가늠하는 열량 지수 (평균·최고기온과 위도 보정)
unit: 지수
dataset: MERRA-2
source: NASA POWER 일별 T2M·T2M_MAX (MERRA-2 2m 평균·최고기온)
start_year: 2001
resolution: 약 50km (MERRA-2 격자 한 칸)
stage: 4/1~9/30 (남반구 10/1~3/31)
stage_from: budburst
stage_to: harvest
condition: Σ [(평균기온−10) + (최고기온−10)] / 2 × 위도 보정계수
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: neutral
station_var: tmean
keywords: [Huglin, 휴글린, 품종, 품종 교체, 재식재, 적합, 어떤 품종, 열량, 기후대, 카베르네, 피노]
---

## 정의
4월 1일~9월 30일(남반구 10월 1일~3월 31일) 동안 매일 [(평균기온−10) + (최고기온−10)] ÷ 2 를 더하고, 낮이 긴 고위도일수록 조금 더 쳐 주는 위도 보정계수를 곱한 값입니다.

## 왜 중요한가
품종마다 익는 데 필요한 Huglin 지수가 대략 정해져 있습니다(예: 피노 누아·리슬링 약 1700, 메를로·카베르네 소비뇽 약 1900, 시라·그르나슈 약 2100). 품종 교체를 고민할 때 "우리 산지가 어느 품종대로 옮겨 가고 있나"를 보는 데 씁니다.

## 해석 가이드
- 기울기가 양수면 더 따뜻한 품종대로 옮겨 가는 중입니다.
- 지수 구간: 1500 미만 매우 서늘, 1500~1800 서늘, 1800~2100 온화, 2100~2400 따뜻, 2400 이상 더움.

## 주의점
- 최고기온을 쓰므로 관측소 대비 최고기온 오차(바로사 약 +2°C 등)가 지수에 그대로 반영됩니다.

## 근거
- 팀 데이터 정리(NASA_와인_데이터정리.xlsx) 2_와인지표_데이터, 7_연도별지표
- Huglin, P. (1978), Nouveau mode d'évaluation des possibilités héliothermiques d'un milieu viticole
- Tonietto & Carbonneau (2004), A multicriteria climatic classification system for grape-growing regions — https://doi.org/10.1016/j.agrformet.2003.06.001
