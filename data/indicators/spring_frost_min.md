---
id: spring_frost_min
name: Spring minimum temperature
category: temp_frost
order: 30
short: The minimum temperature on the coldest day of the budburst season in spring (Apr–May; Southern Hemisphere Oct–Nov); shows how severe frost gets
unit: °C
dataset: MERRA-2
source: NASA POWER daily T2M_MIN (MERRA-2 2 m minimum temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Spring (Apr 1–May 31; Southern Hemisphere Oct 1–Nov 30)
condition: (no condition) minimum over the period
threshold:
threshold_unit:
threshold_options: []
aggregation: min
robust: false
higher_is: better
station_var: tmin
keywords: [spring frost, late frost, frost severity, freeze damage, below freezing, shoots, coldest night, cold injury]
---

## Definition
The lowest daily minimum temperature in spring (Northern Hemisphere April 1–May 31, Southern Hemisphere October 1–November 30). If frost days tell you "how often", this tells you "how hard".

## Why it matters
Young shoots are badly damaged below −2°C. Even with the same number of frost days, damage grows if the coldest night gets colder, so this is used to judge whether equipment such as frost fans or sprinklers is needed.

## How to read
- A positive slope means the coldest spring night is getting less cold.
- Read it together with frost days after budburst.

## Caveats
- Cold air on valley floors is not captured well by a 50 km grid, so actual vineyards may be colder.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
