---
id: flowering_rain
name: Flowering rainfall
category: rain_water
order: 60
short: Total rain in the flowering month (June; Southern Hemisphere December). More rain means poorer fruit set
unit: mm
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR (MERRA-2 observation-corrected precipitation)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Flowering (Jun; Southern Hemisphere Dec)
condition: (no condition) total over the period
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: worse
keywords: [flowering, bloom, fruit set, coulure, shatter, rainy season, rain, yield]
---

## Definition
The total rain that fell during the month grapevines flower (June in the Northern Hemisphere, December in the Southern Hemisphere).

## Why it matters
Rain during flowering washes away pollen, so fewer berries set (coulure, or "shatter") and bunches end up loose and sparse. It is used for yield forecasting and variety choice in regions where flowering overlaps the monsoon rainy season, such as Yeongdong, where the rains begin in June.

## How to read
- A positive slope means flowering is getting wetter.

## Caveats
- Actual flowering dates and the start of the rainy season vary from year to year, so a fixed one-month window is an approximation.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
