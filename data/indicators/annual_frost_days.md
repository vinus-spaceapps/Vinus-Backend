---
id: annual_frost_days
name: Annual frost days
category: temp_frost
order: 90
short: Number of days in one season-year when the minimum temperature was 0°C or below
unit: "days"
dataset: MERRA-2
source: NASA POWER daily T2M_MIN
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Season-year (previous Oct–Sep; Southern Hemisphere previous Apr–Mar)
condition: daily minimum temperature ≤ 0°C
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
station_var: tmin
keywords: [frost, frost days, below freezing, freezing nights, cold, annual frost, yearly]
---

## Definition
The number of days in one season-year (October of the previous year to September; Southern Hemisphere: April of the previous year to March) when the daily minimum temperature was 0°C or below.

## Why it matters
The simplest indicator of how cold a region is overall. When frost days drop sharply, the range of grape varieties the region can grow widens.

## How to read
- A negative slope means frost days are becoming fewer. Read it alongside the spring frost indicators to see *when* in the year frost has declined.

## Caveats
- In the Okanagan, grid temperatures run about 5°C colder than the weather station, so cold indicators may be inflated.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
