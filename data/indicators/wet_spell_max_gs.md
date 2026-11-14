---
id: wet_spell_max_gs
name: Longest wet spell (growing season)
category: rain_water
order: 170
short: Longest run of consecutive rainy days during the growing season
unit: "days"
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Longest run of consecutive days with daily precipitation ≥ 1 mm
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [wet spell, consecutive rain, rainy season, spraying, disease, leaf wetness]
---

## Definition
The longest run of consecutive growing-season days with 1 mm or more of daily rain.

## Why it matters
When rain continues for days, there is no window to spray, and leaves stay wet so disease spreads explosively. It is used for spray planning and decisions on disease-resistant varieties.

## How to read
- A positive slope means long rainy spells are becoming more common.

## Caveats
- Model precipitation tends to produce light rain more often than actually occurs.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
