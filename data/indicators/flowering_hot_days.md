---
id: flowering_hot_days
name: Hot days at flowering
category: heat
order: 90
short: Number of days in the flowering month (June) with a maximum temperature at or above the threshold (default 32°C)
unit: "days"
dataset: MERRA-2
source: NASA POWER daily T2M_MAX
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Flowering (June; Southern Hemisphere December)
condition: daily maximum temperature ≥ threshold
threshold: 32
threshold_unit: °C
threshold_options: [30, 32, 35]
aggregation: count
robust: false
higher_is: worse
station_var: tmax
keywords: [flowering, bloom, flowers, fruit set, heat, pollen, hot days at bloom]
---

## Definition
The number of days during flowering with a daily maximum temperature at or above the threshold (default 32°C). You can switch to 30 or 35°C.

## Why it matters
If it is too hot when the flowers open, the pollen loses its strength and fewer berries set. Used together with cold days at flowering to estimate that year's fruit set (and so the yield).

## How to read
- A positive slope means more heat during flowering.

## Caveats
- The actual flowering date varies by year and by variety, so a fixed one-month window is an approximation.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
