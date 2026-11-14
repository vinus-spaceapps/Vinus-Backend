---
id: gs_tmax_mean
name: Growing-season mean maximum temperature
category: heat
order: 50
short: Average daily maximum temperature over the growing season; the level of daytime heat
unit: "°C"
dataset: MERRA-2
source: NASA POWER daily T2M_MAX
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
station_var: tmax
keywords: [daytime temperature, maximum temperature, daily high, midday heat, heat, photosynthesis, hot afternoons]
---

## Definition
The average of the daily maximum temperatures over the growing season.

## Why it matters
Even with the same mean temperature, hotter days mean more hours when photosynthesis shuts down at midday. Used together with the growing-season mean minimum temperature to tell whether it is the daytime heat or the night-time temperature that is rising.

## How to read
- A positive slope means days are getting hotter.

## Caveats
- As a 50 km grid average, it does not reflect differences in elevation or slope.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
