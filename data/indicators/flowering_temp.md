---
id: flowering_temp
name: Flowering-period mean temperature
category: growth
order: 80
short: Daily mean temperature in the flowering month (June; Southern Hemisphere December), which affects how well berries set (fruit set)
unit: °C
dataset: MERRA-2
source: NASA POWER daily T2M (MERRA-2 2 m mean temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Flowering (June; Southern Hemisphere December)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [flowering, bloom, fruit set, coulure, poor fruit set, bunches, yield]
---

## Definition
The average of the daily mean temperature in the month when grapevines flower (June in the Northern Hemisphere, December in the Southern Hemisphere).

## Why it matters
If it is too cold (roughly below 15°C) or too hot at bloom, pollination fails and fewer berries set (poor fruit set, or coulure). Used to gauge that year's yield and to avoid varieties with unreliable fruit set.

## How to read
- Roughly 20–25°C is good for fruit set. Watch whether values are drifting away from this range.

## Caveats
- Actual flowering dates vary by year and by variety, so a fixed one-month window is an approximation.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
