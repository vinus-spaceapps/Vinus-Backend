---
id: flowering_wet_days
name: Rainy days at flowering
category: rain_water
order: 70
short: Number of days with rain (1 mm or more) during the flowering month (June)
unit: "days"
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Flowering (Jun; Southern Hemisphere Dec)
condition: Daily precipitation ≥ 1 mm
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [flowering, bloom, rainy days, coulure, fruit set, rain, yield]
---

## Definition
The number of days during flowering with 1 mm or more of rain.

## Why it matters
Frequent rain during flowering prevents pollination, so fewer berries set (coulure). It is used together with flowering rainfall (the amount) to estimate that year's yield.

## How to read
- A positive slope means rain at flowering is becoming more frequent.

## Caveats
- Actual flowering dates vary from year to year, so a fixed one-month window is an approximation.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
