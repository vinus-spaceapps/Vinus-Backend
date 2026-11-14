---
id: gs_rain_total
name: Growing-season rainfall
category: rain_water
order: 110
short: Total rain during the growing season
unit: mm
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR (MERRA-2 observation-corrected precipitation)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: (no condition) total over the period
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: neutral
keywords: [rainfall, rain, precipitation, drought, water, irrigation, rainy season, annual rainfall]
---

## Definition
The total rain that fell during the growing season.

## Why it matters
Too little growing-season rain means irrigation is needed; too much brings disease and excessive leaf growth. It is used for irrigation investment and spray (disease-control) planning.

## How to read
- Year-to-year variation is large, so look at extreme years (droughts, monsoon rains) alongside the trend. Viewing it with harvest rainfall and the longest dry spell shows "when" rainfall changed.

## Caveats
- MERRA-2 precipitation is model output corrected with observations, so it can underestimate localized downpours.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
