---
id: spring_windy_days
name: Spring windy days
category: sun_wind
order: 80
short: Number of windy days in the early growing season (Apr–Jun) with a daily mean wind speed at or above the threshold (default 5 m/s)
unit: "days"
dataset: MERRA-2
source: NASA POWER daily WS2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Early growing season (Apr–Jun; Southern Hemisphere Oct–Dec)
condition: Daily mean wind speed ≥ threshold
threshold: 5
threshold_unit: m/s
threshold_options: [4, 5, 6]
aggregation: count
robust: false
higher_is: worse
keywords: [strong wind, windy days, high wind, broken shoots, shoot damage, windbreak, gusts]
---

## Definition
The number of days in the early growing season (Apr–Jun; Southern Hemisphere Oct–Dec) when the daily mean wind speed was at or above the threshold (default 5 m/s). You can switch the threshold to 4 or 6 m/s.

## Why it matters
Young shoots snap easily in strong winds, and that year's bunches are lost with them. Used to decide on windbreak netting and when to do shoot positioning (tying shoots to the trellis).

## How to read
- A positive slope (upward trend) means strong spring winds are becoming more frequent.

## Caveats
- Based on daily mean wind speed, so brief gusts are not captured.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
