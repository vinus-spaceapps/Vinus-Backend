---
id: harvest_wet_spell
name: Longest wet spell at harvest
category: rain_water
order: 50
short: Longest run of consecutive rainy days during the harvest period (Aug–Sep)
unit: "days"
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: Longest run of consecutive days with daily precipitation ≥ 1 mm
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [wet spell, consecutive rain, rainy season, autumn rains, harvest delay, rot]
---

## Definition
The longest run of consecutive harvest-period days with 1 mm or more of daily rain.

## Why it matters
When rain continues for days, grapes never get a chance to dry, rot spreads rapidly and harvest has to be postponed. It is used to judge how much slack the harvest schedule needs and when to spray.

## How to read
- A positive slope means rainy spells at harvest are getting longer.

## Caveats
- Model precipitation tends to produce light rain more often than actually occurs.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
