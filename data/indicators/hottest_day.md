---
id: hottest_day
name: Hottest day of the growing season
category: heat
order: 40
short: The maximum temperature on the hottest day of the growing season
unit: "°C"
dataset: MERRA-2
source: NASA POWER daily T2M_MAX
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: (no condition) highest daily maximum temperature in the period
threshold:
threshold_unit:
threshold_options: []
aggregation: max
robust: false
higher_is: worse
station_var: tmax
keywords: [maximum temperature, hottest day, heatwave, extreme heat, peak temperature, sunburn, leaf scorch]
---

## Definition
The highest daily maximum temperature during the growing season.

## Why it matters
A single bout of extreme heat (around 40°C) can scorch leaves and cook the berries. Used for heatwave-protection investment decisions such as shade nets and irrigation.

## How to read
- A positive slope means the hottest day is getting hotter.

## Caveats
- As a 50 km grid average, it does not reflect differences in elevation or slope.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
