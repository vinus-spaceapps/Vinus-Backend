---
id: gs_tmin_mean
name: Growing-season mean minimum temperature
category: growth
order: 150
short: Average of the daily minimum temperature over the growing season — the level of night temperatures
unit: "°C"
dataset: MERRA-2
source: NASA POWER daily T2M_MIN
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
station_var: tmin
keywords: [night temperature, minimum temperature, warm nights, acidity, aroma, warming]
---

## Definition
The average of the daily minimum temperature over the growing season.

## Why it matters
Warming often heats the nights faster than the days. Warmer nights reduce acidity and aroma, which has a big effect on quality, so this is used together with the growing-season mean maximum temperature.

## How to read
- A positive slope (upward trend) means nights are getting warmer.

## Caveats
- Because it is a 50 km grid average, differences in elevation and hillside position are not captured.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
