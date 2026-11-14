---
id: cool_night_index
name: Cool night index
category: growth
order: 110
short: Mean daily minimum temperature in the month before harvest (September; Southern Hemisphere March)
unit: °C
dataset: MERRA-2
source: NASA POWER daily T2M_MIN (MERRA-2 2 m minimum temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: September (Southern Hemisphere March)
stage_from: veraison
stage_to: harvest
condition: (no condition) monthly mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
station_var: tmin
keywords: [night, nighttime, warm nights, night temperature, diurnal range, acidity, aroma, color, cool nights, cool night index]
---

## Definition
The average of the daily minimum temperature in the last month of ripening (September in the Northern Hemisphere, March in the Southern Hemisphere). It is the same as the Cool Night Index used in wine climate classification.

## Why it matters
Cool nights during ripening help grapes hold on to their aroma, acidity and color. When nights get warmer, acidity drops quickly and aromas fade. Used when considering changing varieties, adjusting harvest timing, or securing higher-elevation vineyard sites.

## How to read
- A positive slope (upward trend) means nights during ripening are getting warmer.
- Classes: 12°C or below, very cool nights; 12–14°C, cool nights; 14–18°C, temperate nights; above 18°C, warm nights.

## Caveats
- It is a one-month average, so if that year's harvest was over before September, it may not line up with the actual ripening period.

## References
- Team data workbook: sheets 2 (wine indicator data) and 7 (indicators by year)
- Tonietto & Carbonneau (2004) — https://doi.org/10.1016/j.agrformet.2003.06.001
