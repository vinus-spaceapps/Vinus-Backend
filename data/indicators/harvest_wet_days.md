---
id: harvest_wet_days
name: Rainy days at harvest
category: rain_water
order: 30
short: Number of days with rain (1 mm or more) during the harvest period (Aug–Sep)
unit: "days"
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: Daily precipitation ≥ 1 mm
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [harvest rain, rainy days, gray mold, botrytis, rot, harvest schedule, rain cover]
---

## Definition
The number of harvest-period days with 1 mm or more of rain.

## Why it matters
When ripe grapes get wet often, gray mold (botrytis) spreads and it becomes hard to find a day to pick. It is used for planning harvest crews and schedules and for decisions on rain covers.

## How to read
- A positive slope means rain at harvest is becoming more frequent. Look at it together with heavy rain days at harvest.

## Caveats
- Model precipitation tends to produce light rain more often than actually occurs.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
