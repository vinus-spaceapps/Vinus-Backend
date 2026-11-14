---
id: topsoil_moisture
name: Topsoil moisture (growing season)
category: drought
order: 110
short: Average wetness of the topsoil (surface layer) during the growing season (0 = dry, 1 = saturated)
unit: "0–1"
dataset: MERRA-2
source: NASA POWER daily GWETTOP
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: (no condition) mean over the period
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: better
keywords: [topsoil, surface soil, soil moisture, drought, cover crop, mulch, young vines]
---

## Definition
The wetness of the topsoil (surface layer), on a 0–1 scale, averaged over the growing season.

## Why it matters
Topsoil responds quickly to rain, so it shows short droughts first. It is used for decisions on irrigating young vines and shallow-rooted varieties, and on cover-crop management.

## How to read
- A negative slope means the topsoil is drying out. Look at it together with root-zone soil moisture (deeper soil).

## Caveats
- These are model values and differ from actual values in an irrigated vineyard.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
