---
id: winter_warm_days
name: Unusually warm winter days
category: temp_frost
order: 150
short: Number of winter days as warm as spring, with a maximum temperature at or above the threshold (default 15°C)
unit: "days"
dataset: MERRA-2
source: NASA POWER daily T2M_MAX
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Winter (Dec–Feb; Southern Hemisphere Jun–Aug)
condition: daily maximum temperature ≥ threshold
threshold: 15
threshold_unit: °C
threshold_options: [10, 15]
aggregation: count
robust: false
higher_is: worse
station_var: tmax
keywords: [warm winter days, winter warm spell, unusual warmth, cold hardiness, winter thaw, deacclimation, freeze damage]
---

## Definition
The number of winter days with a daily maximum temperature at or above the threshold (default 15°C). You can switch to 10°C.

## Why it matters
A few warm days in midwinter can make vines drop their cold hardiness (the resistance to cold they build up for winter), so a cold wave that follows does serious damage. Used for winter protection in regions where cold waves often follow warm spells.

## How to read
- A positive slope means unusually warm winter days are becoming more frequent. Read it together with winter severe cold days.

## Caveats
- As a 50 km grid average, it does not reflect differences in elevation or slope.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
