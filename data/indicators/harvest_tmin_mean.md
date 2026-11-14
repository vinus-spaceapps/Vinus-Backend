---
id: harvest_tmin_mean
name: Harvest-period mean minimum temperature
category: growth
order: 140
short: Average of the daily minimum temperature during harvest (Aug–Sep) — night temperatures during ripening
unit: "°C"
dataset: MERRA-2
source: NASA POWER daily T2M_MIN
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
station_var: tmin
keywords: [harvest nights, minimum temperature, cool nights, warm nights, color, aroma, acidity]
---

## Definition
The average of the daily minimum temperature during the harvest period.

## Why it matters
Cool nights during ripening preserve color, aroma and acidity. It covers two months, longer than the cool night index (September only), so it is less swayed by year-to-year differences.

## How to read
- A positive slope (upward trend) means nights during ripening are getting warmer.

## Caveats
- Because it is a 50 km grid average, differences in elevation and hillside position are not captured.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
