---
id: thermal_gs_length
name: Growing season length (temperature-based)
category: growth
order: 220
short: Length of the thermal growing season, when the mean temperature is 10°C or above
unit: "days"
dataset: MERRA-2
source: NASA POWER daily T2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season start date to end date
condition: Growing season end date − start date
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: neutral
station_var: tmean
keywords: [growing season length, season length, long season, variety, late-ripening varieties]
---

## Definition
The number of days from the temperature-based growing season start date to the end date.

## Why it matters
A longer growing season makes it possible to grow later-ripening varieties, but your current varieties may ripen too quickly. It is a basic input for decisions on changing varieties.

## How to read
- A positive slope (upward trend) means the growing season is getting longer.

## Caveats
- In warm regions (Barossa, Napa), temperatures exceed 10°C even in winter, so the season comes out very long.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
