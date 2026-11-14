---
id: gs_heavy_rain_days
name: Heavy rain days (growing season)
category: rain_water
order: 130
short: Number of growing-season days with daily rain at or above the threshold (default 30 mm)
unit: "days"
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Daily precipitation ≥ threshold
threshold: 30
threshold_unit: mm
threshold_options: [20, 30, 50]
aggregation: count
robust: false
higher_is: worse
keywords: [heavy rain, downpour, cloudburst, storm, soil erosion, drainage, runoff]
---

## Definition
The number of growing-season days with daily rain at or above the threshold (default 30 mm). You can switch it to 20 or 50 mm.

## Why it matters
Heavy rain washes soil off sloping vineyards, spreads disease and overwhelms drainage. It is used to plan investment in drainage channels and slope management.

## How to read
- A positive slope means heavy rain is becoming more frequent.

## Caveats
- Precipitation from a 50 km grid model greatly underestimates localized downpours.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
