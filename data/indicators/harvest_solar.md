---
id: harvest_solar
name: Harvest-period solar radiation
category: sun_wind
order: 20
short: Daily average of the sunlight energy reaching the ground during harvest (Aug–Sep)
unit: "MJ/m²/day"
dataset: CERES
source: NASA POWER daily ALLSKY_SFC_SW_DWN (CERES)
start_year: 2001
resolution: ~100 km (CERES 1° grid)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
keywords: [sunlight, solar radiation, harvest, ripening, sugar, color, sunburn]
---

## Definition
The average daily solar radiation (MJ/m²) during the harvest period, from NASA CERES satellite data.

## Why it matters
Sunlight during ripening builds sugar and color, but if it is too strong the bunches get burned. Used to decide how much leaf to pull and whether to shade.

## How to read
- A positive slope (upward trend) means the ripening period is getting sunnier.

## Caveats
- Values come from the CERES 1° grid.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
