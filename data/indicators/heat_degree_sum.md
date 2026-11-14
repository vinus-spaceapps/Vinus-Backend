---
id: heat_degree_sum
name: Heat accumulation
category: heat
order: 30
short: Sum of how far the maximum temperature went above the threshold (default 35°C) over the growing season; the total amount of heat damage
unit: "°C·days"
dataset: MERRA-2
source: NASA POWER daily T2M_MAX
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Σ max(0, daily maximum temperature − threshold)
threshold: 35
threshold_unit: °C
threshold_options: [32, 35]
aggregation: sum
robust: false
higher_is: worse
station_var: tmax
keywords: [heat accumulation, heat stress, heatwave intensity, heat damage, extreme heat, cumulative heat]
---

## Definition
The sum, over every growing-season day, of how far the daily maximum temperature went above the threshold (default 35°C) (e.g., a day at 38°C counts as 3). You can switch to 32°C.

## Why it matters
If heatwave days tell you "how many days", this tells you "how intense". It reflects the fact that one 40°C day does far more damage than one 36°C day, and is used to gauge how much to invest in heatwave protection.

## How to read
- A positive slope means the total amount of heat damage is growing.

## Caveats
- As a 50 km grid average, it does not reflect differences in elevation or slope.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
