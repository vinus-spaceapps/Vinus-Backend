---
id: rain_intensity_gs
name: Rain intensity (growing season)
category: rain_water
order: 160
short: Average rain per rainy day during the growing season. How hard the rain falls
unit: "mm/day"
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Total rain on wet days (≥1 mm) ÷ number of wet days
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
keywords: [rain intensity, hard rain, downpour, soil erosion, runoff, drainage, cover crop]
---

## Definition
The total rain on rainy days (1 mm or more) during the growing season, divided by the number of rainy days.

## Why it matters
Even with the same total, rain that falls hard all at once runs off instead of soaking in, so the vines end up short of water while the soil gets washed away. It is used for decisions on cover crops and drainage.

## How to read
- A positive slope means rain is falling harder.

## Caveats
- MERRA-2 precipitation is model output corrected with observations, so it can underestimate local rain.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
