---
id: autumn_mean_temp
name: Autumn mean temperature
category: growth
order: 180
short: Daily mean temperature in the autumn after harvest (Oct–Nov; Southern Hemisphere Apr–May), when the canes mature
unit: "°C"
dataset: MERRA-2
source: NASA POWER daily T2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Autumn (Oct–Nov; Southern Hemisphere Apr–May)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [autumn, fall, cane lignification, cane maturity, winter hardiness, overwintering, post-harvest]
---

## Definition
The average of the daily mean temperature over the two autumn months after harvest (Oct–Nov; Southern Hemisphere Apr–May).

## Why it matters
Canes have to mature fully in autumn (cane lignification, when green shoots turn woody) to survive winter cold. If autumn is too warm, maturing is delayed and vines become vulnerable to early-winter cold snaps, so this is used for winter-protection planning.

## How to read
- A positive slope (upward trend) means autumns are getting warmer.

## Caveats
- Because it is a 50 km grid average, differences in elevation and hillside position are not captured.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
