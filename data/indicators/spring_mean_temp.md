---
id: spring_mean_temp
name: Spring mean temperature
category: growth
order: 70
short: Daily mean temperature over the three spring months (Mar–May; Southern Hemisphere Sep–Nov) — the temperature that sets when buds break
unit: °C
dataset: MERRA-2
source: NASA POWER daily T2M (MERRA-2 2 m mean temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Spring (Mar–May; Southern Hemisphere Sep–Nov)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [spring, spring temperature, budburst timing, buds, earlier spring, early spring, warm spring]
---

## Definition
The average of the daily mean temperature over the three spring months (Mar–May in the Northern Hemisphere, Sep–Nov in the Southern Hemisphere).

## Why it matters
The warmer the spring, the earlier buds break. If spring warms up quickly while late frosts stay the same, frost damage grows, so this is used together with the green-up date and frost indicators to decide on frost protection.

## How to read
- A positive slope (upward trend) means spring is warming and buds are breaking earlier. Check whether it moves in the same direction as the green-up date.

## Caveats
- A 50 km grid average.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
