---
id: ice_days
name: Winter ice days
category: temp_frost
order: 140
short: Number of winter days that stayed below freezing even in the daytime (maximum temperature 0°C or below)
unit: "days"
dataset: MERRA-2
source: NASA POWER daily T2M_MAX
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Winter (Dec–Feb; Southern Hemisphere Jun–Aug)
condition: daily maximum temperature ≤ 0°C
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
station_var: tmax
keywords: [ice days, freezing all day, below freezing, frozen ground, deep freeze, cold wave, hard freeze]
---

## Definition
The number of winter days when the daily maximum temperature was 0°C or below, meaning it stayed frozen all day.

## Why it matters
A run of days below freezing all day can freeze the ground deeply and damage the roots and lower trunk. Used to decide on winter protection such as hilling up (mounding soil over the base of the vine) and root protection.

## How to read
- A negative slope means days that stay frozen all day are becoming fewer.

## Caveats
- In the Okanagan, grid temperatures run about 5°C colder than the weather station, so cold indicators may be inflated.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
