---
id: max_daily_rain
name: Max daily rain (growing season)
category: rain_water
order: 140
short: The most rain that fell on a single day during the growing season. A measure of downpour intensity
unit: mm
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR (MERRA-2 observation-corrected precipitation)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: (no condition) highest daily precipitation in the period
threshold:
threshold_unit:
threshold_options: []
aggregation: max
robust: false
higher_is: worse
keywords: [cloudburst, downpour, heavy rain, daily maximum, flooding, soil erosion, typhoon]
---

## Definition
The highest single-day rainfall during the growing season.

## Why it matters
A single cloudburst can wash soil off sloping vineyards, burst bunches and overwhelm drainage. It is used for investment in drainage channels and slope management, and for insurance decisions.

## How to read
- A positive slope means downpours are getting more intense. It swings a lot from year to year, so look at the extreme years as well.

## Caveats
- Precipitation from a 50 km grid model greatly underestimates localized downpours. The actual maximum in a vineyard can be higher.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
