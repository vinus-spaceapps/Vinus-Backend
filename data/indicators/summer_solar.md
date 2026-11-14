---
id: summer_solar
name: Summer solar radiation
category: sun_wind
order: 30
short: Daily average of the sunlight energy reaching the ground during one summer month (July; Southern Hemisphere January)
unit: "MJ/m²/day"
dataset: CERES
source: NASA POWER daily ALLSKY_SFC_SW_DWN (CERES)
start_year: 2001
resolution: ~100 km (CERES 1° grid)
stage: Summer (July; Southern Hemisphere January)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
keywords: [sunlight, solar radiation, summer, rainy season, monsoon, cloudy, photosynthesis]
---

## Definition
The average daily solar radiation (MJ/m²) over one summer month.

## Why it matters
Summer sunlight, while the berries are growing, sets how much photosynthesis the vine can do. Used to explain swings in yield and quality in regions where summers are often clouded over by the rainy season (monsoon).

## How to read
- A negative slope (downward trend) means summers are getting cloudier.

## Caveats
- Values come from the CERES 1° grid.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
