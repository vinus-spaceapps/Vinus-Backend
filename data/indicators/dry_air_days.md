---
id: dry_air_days
name: Dry-air days
category: drought
order: 70
short: Number of growing-season days when daily mean humidity is below 40%
unit: "days"
dataset: MERRA-2
source: NASA POWER daily RH2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Daily mean relative humidity < 40%
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [dry air, low humidity, arid, sunburn, water stress, shading]
---

## Definition
The number of growing-season days when daily mean relative humidity was below 40%.

## Why it matters
In very dry air, leaves and berries lose water quickly, so berries stay small and sunburn damage increases. On the other hand, disease decreases. It is used for irrigation and shading decisions.

## How to read
- A positive slope means dry days are becoming more common.

## Caveats
- An approximation based on daily mean values.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
