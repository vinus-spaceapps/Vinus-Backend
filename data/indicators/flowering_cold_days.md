---
id: flowering_cold_days
name: Flowering-period cold days
category: growth
order: 90
short: Number of cool days during the flowering month (June) with a mean temperature below 15°C
unit: "days"
dataset: MERRA-2
source: NASA POWER daily T2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Flowering (June; Southern Hemisphere December)
condition: Daily mean temperature < 15°C
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
station_var: tmean
keywords: [flowering, bloom, cold, cool weather, coulure, poor fruit set, fruit set]
---

## Definition
The number of days during flowering when the daily mean temperature was below 15°C.

## Why it matters
Cool weather at bloom slows pollination and fewer berries set (poor fruit set, or coulure), leaving loose, sparse bunches. Used for yield forecasting and variety choice in cool regions.

## How to read
- A negative slope (downward trend) means fewer cold days at flowering.

## Caveats
- Actual flowering dates vary from year to year, so a fixed one-month window is an approximation.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
