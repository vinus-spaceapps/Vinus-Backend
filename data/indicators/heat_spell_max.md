---
id: heat_spell_max
name: Longest heatwave
category: heat
order: 20
short: The longest run of consecutive growing-season days with a maximum temperature at or above the threshold (default 35°C)
unit: days
dataset: MERRA-2
source: NASA POWER daily T2M_MAX (MERRA-2 2 m maximum temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: longest run of days with daily maximum temperature ≥ threshold
threshold: 35
threshold_unit: °C
threshold_options: [30, 35]
aggregation: count
robust: false
higher_is: worse
station_var: tmax
keywords: [heatwave, consecutive hot days, heat spell, prolonged heat, sunburn, leaf scorch, berry shrivel, heat stress]
---

## Definition
The longest stretch of consecutive days in the growing season with a daily maximum temperature at or above the threshold (default 35°C).

## Why it matters
Hot days that run on for several days in a row cause much more leaf drying and berry shriveling than hot days that come scattered. Used for decisions on shade nets, irrigation and heat-tolerant varieties.

## How to read
- A positive slope means heatwaves are lasting longer. Read it together with growing-season heatwave days.

## Caveats
- Cool regions have almost no 35°C days, so many years are 0. Check the 30°C threshold as well.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
