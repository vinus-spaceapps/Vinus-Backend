---
id: harvest_rain_days
name: Heavy rain days at harvest
category: rain_water
order: 20
short: Number of harvest-period days (Aug–Sep; Southern Hemisphere Feb–Mar) with daily rain at or above the threshold
unit: days
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR (MERRA-2 observation-corrected precipitation)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
stage_from: veraison
stage_to: harvest
condition: Daily precipitation ≥ threshold
threshold: 20
threshold_unit: mm
threshold_options: [10, 20, 30]
aggregation: count
robust: false
higher_is: worse
keywords: [rain, harvest rain, heavy rain, rot, gray mold, botrytis, berry splitting, typhoon, rain cover]
---

## Definition
The number of days during harvest (August–September in the Northern Hemisphere, February–March in the Southern Hemisphere) with daily rain at or above the threshold (default 20 mm). You can switch it to 10 mm or 30 mm.

## Why it matters
Heavy rain just before harvest makes berries burst (berry splitting) and spreads gray mold (botrytis), forcing growers to pick early before sugar has fully built up. It is used for harvest planning, investment in rain covers, and considering early-ripening varieties.

## How to read
- A positive slope means heavy rain at harvest is becoming more frequent.
- It is a small whole number between 0 and 10, so it swings a lot from year to year. In dry regions (Napa, Okanagan) it is almost always 0. Look at harvest rainfall as well.

## Caveats
- MERRA-2 precipitation is model output corrected with observations, so it can underestimate localized downpours. We plan to cross-check with GPM IMERG (~10 km).

## References
- Team data workbook: sheets "2_Wine indicator data" and "7_Indicators by year"
- NASA POWER — https://power.larc.nasa.gov/
