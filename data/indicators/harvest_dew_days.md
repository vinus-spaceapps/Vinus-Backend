---
id: harvest_dew_days
name: Harvest-period dew days
category: disease
order: 80
short: Number of days during harvest (Aug–Sep) when night temperatures drop close to the dew point, so dew easily forms on the bunches
unit: "days"
dataset: MERRA-2
source: NASA POWER daily T2M, RH2M, T2M_MIN
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: Daily minimum temperature ≤ dew point + 1°C (dew point calculated from mean temperature and humidity)
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [dew, night dew, leaf wetness, wet bunches, mildew, rot, airflow, leaf removal]
---

## Definition
The number of days during the harvest period when the daily minimum temperature fell to or below that day's dew point (calculated from mean temperature and humidity) plus 1°C.

## Why it matters
Even without rain, bunches wet from dew that forms overnight let fungi spread. Used to decide on removing leaves around the bunches (for airflow) and on spraying.

## How to read
- A positive slope (upward trend) means more nights with dew.

## Caveats
- An approximation based on daily mean values.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
