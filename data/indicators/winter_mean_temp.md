---
id: winter_mean_temp
name: Winter mean temperature
category: temp_frost
order: 110
short: Average daily mean temperature in winter (Dec–Feb; Southern Hemisphere Jun–Aug)
unit: "°C"
dataset: MERRA-2
source: NASA POWER daily T2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Winter (Dec–Feb; Southern Hemisphere Jun–Aug)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [winter, warm winter, mild winter, dormancy, overwintering pests, winter temperature]
---

## Definition
The average of the daily mean temperatures over the three winter months.

## Why it matters
A warmer winter means less damage from extreme cold, but more pests survive the winter and dormancy becomes shallower, which leaves vines more vulnerable to spring frost. Used for planning winter protection and pest and disease control.

## How to read
- A positive slope means winters are getting warmer. Read it together with dormancy chill days.

## Caveats
- As a 50 km grid average, it does not reflect differences in elevation or slope.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
