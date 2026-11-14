---
id: soil_drought_days
name: Soil drought days
category: drought
order: 140
short: Number of growing-season days when root-zone soil is drier than the region's usual lowest 20% (2001–2010)
unit: "days"
dataset: MERRA-2
source: NASA POWER daily GWETROOT
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Root-zone soil moisture < the region's 2001–2010 growing-season 20th percentile
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [soil drought, dry soil, drought days, drier than normal, irrigation, soil moisture]
---

## Definition
The number of growing-season days when root-zone soil moisture fell below the bottom-20% mark (20th percentile) of that region's own 2001–2010 growing-season values.

## Why it matters
Soils and climates differ between regions, so "how dry counts as drought" differs too. By counting "days drier than usual" against each region's own baseline, regions can be compared with one another. It is used for irrigation investment decisions.

## How to read
- A positive slope means days drier than usual are becoming more common. By definition, the years 2001–2010 average about 20% of days per year.

## Caveats
- The baseline period (2001–2010) may itself differ from the long-term normal.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
