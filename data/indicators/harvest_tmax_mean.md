---
id: harvest_tmax_mean
name: Harvest-period mean maximum temperature
category: growth
order: 130
short: Average of the daily maximum temperature during harvest (Aug–Sep)
unit: "°C"
dataset: MERRA-2
source: NASA POWER daily T2M_MAX
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
station_var: tmax
keywords: [harvest daytime heat, maximum temperature, hot days, harvest, sugar, aroma, acidity]
---

## Definition
The average of the daily maximum temperature during the harvest period.

## Why it matters
Hot days during ripening push sugar up quickly while aroma and acidity fade. Used to decide whether to bring the harvest forward.

## How to read
- A positive slope (upward trend) means days during ripening are getting hotter.

## Caveats
- Because it is a 50 km grid average, differences in elevation and hillside position are not captured.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
