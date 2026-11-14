---
id: gdd_growing_season
name: Growing-season degree days (GDD)
category: growth
order: 10
short: Sum of how far the daily mean temperature rose above 10°C over the growing season (Apr–Oct; Southern Hemisphere Oct–Apr)
unit: °C·days
dataset: MERRA-2
source: NASA POWER daily T2M (MERRA-2 2 m mean temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
stage_from: budburst
stage_to: harvest
condition: Daily mean temperature − 10°C (values below 0 count as 0)
threshold: 10
threshold_unit: °C
threshold_options: [10]
aggregation: sum
robust: false
higher_is: neutral
station_var: tmean
keywords: [growing degree days, GDD, heat summation, warming, rising temperature, variety, ripening, sugar, Winkler, Winkler index]
---

## Definition
The sum, over the growing season (Apr 1–Oct 31 in the Northern Hemisphere, Oct 1–Apr 30 in the Southern Hemisphere), of how far each day's mean temperature rose above 10°C (e.g., a day averaging 18°C adds 8). It works the same way as the Winkler index used in viticulture.

## Why it matters
Growing degree days are the most basic yardstick for which varieties ripen well in a region. If the value keeps rising, your current varieties may ripen too fast and end up short on acidity, so it is used for replanting (changing varieties) plans.

## How to read
- A positive slope (upward trend) means the region is shifting toward a warmer climate zone. Watch whether it crosses the Winkler region boundaries (1390, 1670, 1940, 2220 °C·days).
- Whether this is good or bad depends on the variety. In cool regions it can even help.

## Caveats
- The growing season is fixed by calendar date, so the effect of actual budburst and harvest moving earlier is left out.
- Compared with nearby weather stations, the grid GDD for Napa comes out slightly higher than observed (Apr–Sep comparison).

## References
- Team data workbook: sheets 2 (wine indicator data), 7 (indicators by year) and 12 (station growing degree days)
- Jones et al. (2010), climate in winegrape growing regions — https://doi.org/10.5344/ajev.2010.61.3.313
