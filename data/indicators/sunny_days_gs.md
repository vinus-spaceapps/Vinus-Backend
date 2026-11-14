---
id: sunny_days_gs
name: Growing-season sunny days
category: sun_wind
order: 50
short: Number of days in the growing season that were clear, with almost no cloud
unit: "days"
dataset: CERES
source: NASA POWER daily ALLSKY_SFC_SW_DWN (CERES)
start_year: 2001
resolution: ~100 km (CERES 1° grid)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Solar radiation ≥ 80% of clear-sky radiation (0.75 × top-of-atmosphere radiation)
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: neutral
keywords: [sunny days, clear days, sunshine, sunlight, clouds, weather]
---

## Definition
The number of days in the growing season when actual solar radiation was at least 80% of what a clear sky could have delivered that day (FAO-56 formula).

## Why it matters
Plenty of clear days helps sugar and color develop, but also raises sunburn and water stress. Used to decide on canopy management, shading and irrigation.

## How to read
- A positive slope (upward trend) means more clear days.

## Caveats
- Values come from the CERES 1° grid.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
