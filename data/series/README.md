# 실제 NASA 집계값 넣는 곳

여기에 CSV를 넣으면 그 변수·산지 조합은 예시 데이터 대신 이 값으로 분석하고, 화면의 "예시 데이터" 배지가 사라집니다.

```
data/series/<변수id>/<산지id>.csv            # 기본 기준값
data/series/<변수id>/<산지id>__t<기준값>.csv  # 다른 기준값 (예: frost_after_budburst/burgundy__t-2.csv)
```

```csv
year,value
2003,4
2004,2
...
```

- `year`는 시즌의 **수확 연도**입니다 (남반구 바로사는 2024년 9월~2025년 3월 시즌 = 2025).
- 값은 지표 md의 조건·생육 단계·집계 방식대로 해마다 하나씩 계산한 숫자입니다.
- 변수 id는 `data/indicators/*.md`, 산지 id는 `data/regions.json`을 보세요.
- Giovanni에서 영역 평균 일별 시계열을 내려받아 집계하면 됩니다.
