---
id: flowering_solar
name: Flowering-period solar radiation
category: sun_wind
order: 40
short: Daily average of the sunlight energy reaching the ground during the flowering month (June)
unit: "MJ/m²/day"
dataset: CERES
source: NASA POWER daily ALLSKY_SFC_SW_DWN (CERES)
start_year: 2001
resolution: ~100 km (CERES 1° grid)
stage: Flowering (June; Southern Hemisphere December)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: better
keywords: [flowering, bloom, fruit set, sunlight, solar radiation, cloudy, coulure, poor fruit set]
---

## Definition
The average daily solar radiation (MJ/m²) during flowering.

## Why it matters
If cloudy days drag on while the vines are in bloom, they run short of carbohydrates and fewer berries set. Used together with flowering-period temperature and rain to gauge that year's fruit set.

## How to read
- A positive slope (upward trend) means flowering is getting sunnier.

## Caveats
- Values come from the CERES 1° grid.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
