---
id: spring_cold_snaps
name: Spring cold snaps
category: temp_frost
order: 50
short: Number of spring days when the daily mean temperature dropped by 5°C or more from the day before
unit: "days"
dataset: MERRA-2
source: NASA POWER daily T2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Spring (Apr 1–May 31; Southern Hemisphere Oct 1–Nov 30)
condition: daily mean temperature 5°C or more below the previous day's
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
station_var: tmean
keywords: [cold snap, sudden cold, spring chill, temperature drop, erratic weather, cold injury, late cold spell]
---

## Definition
The number of days in spring (April–May; Southern Hemisphere October–November) when the daily mean temperature fell by 5°C or more from the previous day.

## Why it matters
When young shoots grow fast in warm weather and it then turns cold suddenly, the shoots can be damaged even without frost, and flower-bud formation can be disrupted. This complements frost-protection and insurance decisions.

## How to read
- A positive slope means sudden swings in spring weather are becoming more frequent.

## Caveats
- As a 50 km grid average, it does not reflect differences in elevation or slope.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
