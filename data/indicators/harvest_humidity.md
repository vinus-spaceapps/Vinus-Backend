---
id: harvest_humidity
name: Harvest-period mean humidity
category: disease
order: 60
short: Average of the daily mean relative humidity during harvest (Aug–Sep; Southern Hemisphere Feb–Mar)
unit: "%"
dataset: MERRA-2
source: NASA POWER daily RH2M (MERRA-2 2 m relative humidity)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
keywords: [humidity, damp, harvest, mildew, gray mold, botrytis, rot, berry splitting]
---

## Definition
The average of the daily mean relative humidity during the harvest period.

## Why it matters
Ripe grapes rot easily from gray mold (botrytis) when the air is humid. Used to decide harvest timing, pre-harvest spraying, and whether to install rain covers.

## How to read
- A positive slope (upward trend) means the harvest period is getting damper. Read it together with harvest-period rainfall and heavy-rain days.

## Caveats
- Because these are daily means, nighttime dew and fog are not captured.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
