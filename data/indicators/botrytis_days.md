---
id: botrytis_days
name: Gray mold risk days
category: disease
order: 30
short: Number of days during harvest (Aug–Sep) with humidity of 85% or more and temperatures of 15–25°C, when gray mold (botrytis) spreads easily
unit: "days"
dataset: MERRA-2
source: NASA POWER daily T2M, RH2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: Relative humidity ≥ 85% and 15°C ≤ mean temperature ≤ 25°C
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [gray mold, grey mold, botrytis, bunch rot, rot, harvest disease, humidity, fungicide]
---

## Definition
The number of days during the harvest period when the daily mean relative humidity was 85% or higher and the mean temperature was 15–25°C.

## Why it matters
Gray mold (botrytis) can rot ripe bunches whole, causing heavy losses right before harvest. Used to decide whether to harvest earlier, spray before harvest, or thin bunches.

## How to read
- A positive slope (upward trend) means the risk of rot at harvest is rising.

## Caveats
- An approximation based on daily mean values.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
