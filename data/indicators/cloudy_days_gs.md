---
id: cloudy_days_gs
name: Growing-season cloudy days
category: sun_wind
order: 60
short: Number of days in the growing season when thick cloud cut sunlight sharply
unit: "days"
dataset: CERES
source: NASA POWER daily ALLSKY_SFC_SW_DWN (CERES)
start_year: 2001
resolution: ~100 km (CERES 1° grid)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Solar radiation < 40% of clear-sky radiation (0.75 × top-of-atmosphere radiation)
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [cloudy days, clouds, overcast, low sunlight, rainy season, sugar, ripening]
---

## Definition
The number of days in the growing season when actual solar radiation was less than 40% of what a clear sky could have delivered that day.

## Why it matters
Runs of cloudy days cut photosynthesis, so sugars build up less, and keep leaves wet longer, so disease spreads. Used to judge quality swings and spraying in regions with a long rainy season.

## How to read
- A positive slope (upward trend) means more cloudy days.

## Caveats
- Values come from the CERES 1° grid.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
