---
id: dtr_growing
name: Growing-season diurnal temperature range
category: growth
order: 170
short: Average difference between the daily maximum and minimum temperature over the growing season
unit: °C
dataset: MERRA-2
source: NASA POWER daily T2M_MAX, T2M_MIN (MERRA-2 2 m maximum and minimum temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: (no condition) period mean of (maximum temperature − minimum temperature)
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: better
station_var: tmean
keywords: [diurnal temperature range, day-night difference, night temperature, aroma, color, acidity, anthocyanins]
---

## Definition
Each day's (maximum temperature − minimum temperature), averaged over the growing season. This is the diurnal temperature range (the gap between day and night temperatures).

## Why it matters
Warm days and cool nights (a large diurnal temperature range) help grapes keep their color, aroma and acidity. When the range shrinks, quality can drop even at the same mean temperature, so it is a reference when choosing varieties and vineyard sites.

## How to read
- A negative slope (downward trend) means nights are warming faster than days.

## Caveats
- With a 50 km grid, values come out smaller than the actual diurnal range in valleys and on hillsides.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
