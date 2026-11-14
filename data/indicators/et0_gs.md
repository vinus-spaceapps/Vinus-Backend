---
id: et0_gs
name: Growing-season evapotranspiration
category: drought
order: 40
short: Total water lost by evaporation from soil and leaves during the growing season (reference evapotranspiration)
unit: "mm"
dataset: MERRA-2
source: NASA POWER daily T2M·T2M_MAX·T2M_MIN
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Σ reference evapotranspiration ET0 (Hargreaves equation, FAO-56)
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: worse
keywords: [evapotranspiration, ET0, water demand, water use, irrigation amount, dry, evaporation]
---

## Definition
The sum of daily reference evapotranspiration (ET0, Hargreaves equation) over the growing season, calculated from temperature and latitude.

## Why it matters
As temperatures rise, more water is lost to evaporation even if rainfall stays the same, so more irrigation is needed. It is used to size irrigation systems and decide how much water to secure.

## How to read
- A positive slope means the atmosphere is drawing more water out of the vineyard.

## Caveats
- The equation does not include wind or humidity, so it differs from actual evapotranspiration.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
