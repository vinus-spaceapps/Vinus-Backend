---
id: frost_free_days
name: Frost-free period
category: growth
order: 230
short: Number of frost-free days between the last spring frost and the first autumn frost
unit: days
dataset: MERRA-2
source: NASA POWER daily T2M_MIN (MERRA-2 2 m minimum temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Last spring frost to first autumn frost
condition: Period between days with a daily minimum temperature ≤ 0°C
threshold: 0
threshold_unit: °C
threshold_options: [0]
aggregation: count
robust: false
higher_is: better
station_var: tmin
keywords: [frost-free period, frost-free days, no frost, growing season length, autumn frost, first frost, late frost, season length]
---

## Definition
The number of days from the day after that year's last spring frost (minimum temperature 0°C or below) to the day before the first autumn frost.

## Why it matters
A long frost-free period is what lets even late-ripening varieties be harvested before frost. Used when considering planting late-ripening varieties or adjusting harvest timing.

## How to read
- A positive slope (upward trend) means the frost-free period is getting longer.

## Caveats
- In regions with almost no frost (Napa in some years, Barossa), many years cannot be calculated.
- The most recent year may be missing because its autumn is not over yet.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
