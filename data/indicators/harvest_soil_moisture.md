---
id: harvest_soil_moisture
name: Soil moisture at harvest
category: drought
order: 130
short: Average root-zone soil wetness during the harvest period (Aug–Sep)
unit: "0–1"
dataset: MERRA-2
source: NASA POWER daily GWETROOT
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: (no condition) mean over the period
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
keywords: [harvest soil moisture, soil water, diluted flavor, drainage, irrigation cutoff, ripening]
---

## Definition
The root-zone soil wetness, on a 0–1 scale, averaged over the harvest period.

## Why it matters
If the soil is too wet during ripening, flavor becomes diluted; if it is too dry, ripening stalls. It is used to decide when to stop irrigating before harvest and whether drainage is needed.

## How to read
- The right level differs by region, so look at the direction of change rather than the absolute value.

## Caveats
- These are model values.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
