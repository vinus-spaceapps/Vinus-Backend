# 연도별 집계값 (실제 NASA 데이터)

여기 있는 CSV가 분석에 쓰이는 실제 값입니다. CSV가 있는 변수·산지 조합은 "NASA 집계" 배지로, 없는 지표(지금은 연기 2개)는 "예시 데이터" 배지로 표시됩니다.

지금 파일들은 팀 엑셀에서 자동으로 만들었습니다. 손으로 고치지 말고, 엑셀을 고친 뒤 다시 만드세요.

```bash
.venv/bin/python scripts/import_team_xlsx.py ~/Downloads/NASA_와인_데이터정리.xlsx
```

## 파일 이름

```
data/series/<변수id>/<산지id>.csv            # 지표 md 의 기본 기준값
data/series/<변수id>/<산지id>__t<기준값>.csv  # 다른 기준값 (예: frost_after_budburst/burgundy__t-2.csv, heat_days/napa__t30.csv)
```

## 형식

```csv
year,value
2001,1
2002,0
```

- `year`는 시즌의 **수확 연도**입니다 (남반구 바로사는 2025년 10월~2026년 4월 시즌 = 2026).
- 값은 지표 md의 조건·기간·집계 방식대로 해마다 하나씩 계산한 숫자입니다. 비어 있는 해는 줄을 빼면 되고, 화면에 "N개 연도가 비어 있어 제외" 안내가 붙습니다.
- 변수 id는 `data/indicators/*.md`, 산지 id는 `data/regions.json`을 보세요.
