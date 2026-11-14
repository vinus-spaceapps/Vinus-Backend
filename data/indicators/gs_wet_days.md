---
id: gs_wet_days
name: Rainy days (growing season)
category: rain_water
order: 120
short: Number of growing-season days with daily rain at or above the threshold (default 1 mm)
unit: days
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR (MERRA-2 observation-corrected precipitation)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Daily precipitation ≥ threshold
threshold: 1
threshold_unit: mm
threshold_options: [1, 5, 10]
aggregation: count
robust: false
higher_is: worse
keywords: [rainy days, wet days, frequent rain, humid, fungal disease, spraying, disease]
---

## Definition
The number of growing-season days with daily rain at or above the threshold (default 1 mm). You can switch it to 5 mm or 10 mm.

## Why it matters
How "often" it rains matters more for fungal disease than the total amount, because disease spreads when leaves get wet often. It is used to plan the number and cost of sprays.

## How to read
- A positive slope means rain is becoming more frequent. Look at it together with humid days (growing season).

## Caveats
- Model precipitation tends to produce light rain more often than actually occurs, so the 1 mm threshold can overcount days. Check the 5 mm threshold as well.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
