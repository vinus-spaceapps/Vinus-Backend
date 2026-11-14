---
id: summer_rain
name: Summer rainfall
category: rain_water
order: 100
short: Total rain in one summer month (July; Southern Hemisphere January). Water while the berries are growing
unit: "mm"
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Summer (Jul; Southern Hemisphere Jan)
condition: (no condition) total over the period
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: neutral
keywords: [summer rain, rainy season, July, berry growth, berry size, drainage, irrigation]
---

## Definition
The total rain over the summer month when the berries swell (July; Southern Hemisphere January).

## Why it matters
Too much rain at this stage makes berries swell so their flavor is diluted and disease spreads; too little leaves berries small. It is especially important in Yeongdong, where the monsoon rains extend into July, and is used for irrigation and drainage decisions.

## How to read
- Year-to-year variation is large. Look at it together with summer water balance.

## Caveats
- MERRA-2 precipitation is model output corrected with observations, so it can underestimate local rain.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
