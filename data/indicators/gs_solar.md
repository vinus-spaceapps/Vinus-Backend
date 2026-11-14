---
id: gs_solar
name: Growing-season solar radiation
category: sun_wind
order: 10
short: Daily average of the sunlight energy reaching the ground during the growing season
unit: MJ/m²/day
dataset: CERES
source: NASA POWER daily ALLSKY_SFC_SW_DWN (CERES satellite surface solar radiation)
start_year: 2001
resolution: ~100 km (CERES 1° grid)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
keywords: [sunlight, solar radiation, sunshine, sunny days, clouds, photosynthesis, sunburn]
---

## Definition
The average sunlight energy (MJ) reaching 1 m² of ground per day during the growing season, under actual weather including clouds. NASA POWER provides the NASA CERES satellite data at a daily time step.

## Why it matters
Sunlight is the source of photosynthesis and sugar build-up. More solar radiation speeds up ripening but also raises the risk of sunburn (sun scald on the berries), so it is used for canopy management (managing the leaves) and decisions on investing in shade nets.

## How to read
- A positive slope (upward trend) means more clear days or less cloud.

## Caveats
- This is CERES data, not MERRA-2. The most recent few days do not have values yet.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
- NASA CERES — https://ceres.larc.nasa.gov/
