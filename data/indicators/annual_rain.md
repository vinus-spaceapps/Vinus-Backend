---
id: annual_rain
name: Annual rainfall
category: rain_water
order: 190
short: Total rain over one season year (previous October to September)
unit: "mm"
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Season year (previous Oct–Sep; Southern Hemisphere previous Apr–Mar)
condition: (no condition) total over the period
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: neutral
keywords: [annual rainfall, yearly rain, water supply, drought, water storage, reservoir, irrigation]
---

## Definition
The total rain that fell over one season year (previous October to September; Southern Hemisphere previous April to March).

## Why it matters
This is the most basic indicator of a region's water situation. When annual rainfall declines, water storage, irrigation infrastructure and secure water rights become more important.

## How to read
- A negative slope means the year as a whole is getting drier. To see "when" in the year rainfall changed, look at the seasonal rainfall indicators.

## Caveats
- MERRA-2 precipitation is model output corrected with observations, so it can underestimate local rain.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
