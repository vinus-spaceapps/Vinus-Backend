---
id: heat_days
name: Growing-season heatwave days
category: heat
order: 10
short: Number of days in the growing season (Apr–Oct; Southern Hemisphere Oct–Apr) with a maximum temperature at or above the threshold
unit: days
dataset: MERRA-2
source: NASA POWER daily T2M_MAX (MERRA-2 2 m maximum temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
stage_from: budburst
stage_to: harvest
condition: daily maximum temperature ≥ threshold
threshold: 35
threshold_unit: °C
threshold_options: [30, 32, 35, 38]
aggregation: count
robust: false
higher_is: worse
station_var: tmax
keywords: [heatwave, heat, hot days, extreme heat, sunburn, berry sunburn, scorching, heat stress]
---

## Definition
The number of days in the growing season (Northern Hemisphere April 1–October 31, Southern Hemisphere October 1–April 30) with a daily maximum temperature at or above the threshold. The default is 35°C (heatwave); you can switch to 30°C (hot), 32°C or 38°C.

## Why it matters
When days above 35°C keep coming, photosynthesis shuts down, berries get scorched by the sun (sunburn) and acidity drops quickly. Used when weighing a switch to heat-tolerant varieties, investment in shade nets and irrigation, or a change in harvest timing.

## How to read
- A positive slope means heat stress is increasing.
- Cool regions (Mosel, Burgundy) have almost no 35°C days, so many years are 0. For these regions, try switching the threshold to 30°C.

## Caveats
- As a 50 km grid average, it does not reflect differences in slope direction or elevation.
- The maximum-temperature error compared with nearby weather stations differs by region (Barossa about +2°C, Okanagan about −5°C).

## References
- Team data workbook — sheets: wine indicator data, indicators by year
- NASA POWER — https://power.larc.nasa.gov/
