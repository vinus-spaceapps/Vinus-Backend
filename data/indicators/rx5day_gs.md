---
id: rx5day_gs
name: Max 5-day rainfall (growing season)
category: rain_water
order: 150
short: Largest 5-day rain total in the growing season. The size of a single monsoon or typhoon event
unit: "mm"
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: (no condition) highest 5-day consecutive precipitation total
threshold:
threshold_unit:
threshold_options: []
aggregation: max
robust: false
higher_is: worse
keywords: [rainy season, monsoon, typhoon, multi-day rain, flooding, waterlogging, drainage]
---

## Definition
The largest rainfall total over any 5 consecutive days during the growing season.

## Why it matters
It is heavy rain lasting several days, more than a single-day downpour, that floods vineyards and damages roots. It is used to size drainage and to judge flood risk.

## How to read
- A positive slope means single big rain events are getting larger.

## Caveats
- MERRA-2 precipitation is model output corrected with observations, so it can underestimate local rain.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
