---
id: water_balance_harvest
name: Harvest water balance
category: drought
order: 30
short: Harvest-period (Aug–Sep) rain minus the water lost to evaporation
unit: "mm"
dataset: MERRA-2
source: NASA POWER daily T2M·T2M_MAX·T2M_MIN·PRECTOTCORR
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: Σ (precipitation − reference evapotranspiration ET0), Hargreaves equation
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: neutral
keywords: [harvest water, water balance, diluted flavor, irrigation, dry, rot, shriveling]
---

## Definition
The sum of daily (precipitation − reference evapotranspiration) over the harvest period.

## Why it matters
Too much water during ripening dilutes flavor and invites rot; too little makes berries shrivel. It is used for decisions on irrigation just before harvest and on harvest timing.

## How to read
- A positive value means rain exceeds evaporation (wet); a negative value means a water shortage.

## Caveats
- The Hargreaves equation tends to overestimate evapotranspiration in humid places.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
