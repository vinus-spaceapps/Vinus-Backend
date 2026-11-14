---
id: harvest_max_rain
name: Max daily rain at harvest
category: rain_water
order: 40
short: The most rain that fell on a single day during the harvest period (Aug–Sep)
unit: "mm"
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: (no condition) highest daily precipitation in the period
threshold:
threshold_unit:
threshold_options: []
aggregation: max
robust: false
higher_is: worse
keywords: [harvest downpour, heavy rain, typhoon, cloudburst, berry splitting, rot, insurance]
---

## Definition
The highest single-day rainfall during the harvest period.

## Why it matters
Ripe grapes can burst (berry splitting) and start to rot after a single downpour. It is used for insurance and harvest planning in regions where typhoons and cloudbursts arrive at harvest time.

## How to read
- It swings a lot from year to year, so look at the extreme years as well.

## Caveats
- Precipitation from a 50 km grid model greatly underestimates localized downpours.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
