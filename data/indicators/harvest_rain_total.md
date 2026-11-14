---
id: harvest_rain_total
name: Harvest rainfall
category: rain_water
order: 10
short: Total rain during the harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
unit: mm
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR (MERRA-2 observation-corrected precipitation)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
stage_from: veraison
stage_to: harvest
condition: (no condition) total over the period
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: worse
keywords: [rain, harvest rain, rainfall, precipitation, rot, downy mildew, harvest delay, typhoon, rainy season]
---

## Definition
The total rain that fell over the two harvest months (August–September in the Northern Hemisphere, February–March in the Southern Hemisphere).

## Why it matters
A wet harvest spreads fungal disease, makes grapes take up water so their flavor is diluted, and delays picking (Bordeaux 2024). It is used for harvest planning, spray scheduling and investment in rain covers.

## How to read
- A positive slope means harvest is getting wetter.
- In Yeongdong, with its monsoon rains and typhoons, year-to-year differences are very large, so one or two years can drive the trend.

## Caveats
- MERRA-2 precipitation is model output corrected with observations. We plan to cross-check with GPM IMERG (~10 km).

## References
- Team data workbook — sheet "3_Region coordinates" (Bordeaux 2024 rainfall and fungal disease) and sheet "7_Indicators by year"
- NASA POWER — https://power.larc.nasa.gov/
