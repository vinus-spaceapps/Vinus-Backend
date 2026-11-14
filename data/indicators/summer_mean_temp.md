---
id: summer_mean_temp
name: Summer mean temperature
category: growth
order: 100
short: Daily mean temperature over one summer month (July; Southern Hemisphere January) — when berries swell and get ready for veraison
unit: "°C"
dataset: MERRA-2
source: NASA POWER daily T2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Summer (July; Southern Hemisphere January)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [summer, July, veraison, berry growth, berry size, ripening speed]
---

## Definition
The average of the daily mean temperature over one summer month (July; Southern Hemisphere January).

## Why it matters
Temperatures while the berries are swelling set when veraison begins and how fast ripening goes. Used to forecast harvest timing and to judge variety suitability.

## How to read
- A positive slope (upward trend) means summers are getting hotter.

## Caveats
- Because it is a 50 km grid average, differences in elevation and hillside position are not captured.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
