---
id: early_spring_gdd
name: Early-spring growing degree days
category: growth
order: 60
short: Sum of how far the mean temperature rose above 5°C in early spring (Jan–Mar) — the warmth that wakes the buds early
unit: "°C·days"
dataset: MERRA-2
source: NASA POWER daily T2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Early spring (Jan–Mar; Southern Hemisphere Jul–Sep)
condition: Σ max(0, mean temperature − 5°C)
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: worse
station_var: tmean
keywords: [early spring, warm spring, early budburst, budburst, spring frost, late frost, growing degree days]
---

## Definition
The sum, over early spring (Jan–Mar; Southern Hemisphere Jul–Sep), of how far each day's mean temperature rose above 5°C.

## Why it matters
A warm early spring makes buds break sooner, which raises the risk of being hit by a late spring frost afterwards. Used together with the green-up date and frost indicators to decide on frost protection.

## How to read
- A positive slope (upward trend) means buds are waking earlier (more exposure to frost).

## Caveats
- Because it is a 50 km grid average, differences in elevation and hillside position are not captured.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
