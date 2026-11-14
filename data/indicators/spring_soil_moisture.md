---
id: spring_soil_moisture
name: Spring soil moisture
category: drought
order: 120
short: Average root-zone soil wetness in spring (Apr–May). The water that starts the season
unit: "0–1"
dataset: MERRA-2
source: NASA POWER daily GWETROOT
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Spring (Apr 1–May 31; Southern Hemisphere Oct 1–Nov 30)
condition: (no condition) mean over the period
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: better
keywords: [spring soil moisture, soil water, early growth, start of irrigation, budburst, drought]
---

## Definition
The root-zone soil wetness, on a 0–1 scale, averaged over the two spring months.

## Why it matters
New shoots and leaves grow well only when there is enough water in the soil in spring. Low spring soil moisture means early irrigation is needed, so this is used to decide when to start irrigating.

## How to read
- A negative slope means the season is starting with drier soil. Look at it together with dormancy rainfall.

## Caveats
- These are model values.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
