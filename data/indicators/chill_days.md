---
id: chill_days
name: Dormancy chill days
category: temp_frost
order: 160
short: Number of cool days (daily mean 0–7.2°C) during dormancy (Nov–Mar; Southern Hemisphere May–Sep) that vines need to wake up from their winter rest
unit: days
dataset: MERRA-2
source: NASA POWER daily T2M (MERRA-2 2 m mean temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Dormancy (Nov–Mar; Southern Hemisphere May–Sep)
condition: 0°C < daily mean temperature ≤ 7.2°C
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: better
station_var: tmean
keywords: [chilling, chill requirement, dormancy, winter rest, poor budburst, uneven budburst, warm winter, chill hours]
---

## Definition
The number of days during dormancy when the daily mean temperature was above 0°C and at or below 7.2°C. It is a simple day-by-day version of the "chill hours" used in fruit-tree research.

## Why it matters
Grapevines need a certain stretch of cool winter weather to break bud evenly in spring. If winter is too warm, budburst can be patchy and yields can fall, so this is used for variety and vineyard-management decisions in warm regions.

## How to read
- A negative slope means winters are getting warmer and chilling is falling short.
- Grapes need less chilling than most other fruit crops, so this matters most in warm regions such as Barossa and Napa.

## Caveats
- The original metric is counted in hours, so using a daily mean is an approximation.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
