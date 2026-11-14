---
id: vpd_mean
name: Growing-season vapor pressure deficit (VPD)
category: drought
order: 50
short: Average of how dry the air is during the growing season, i.e. how hard it pulls water from leaves (higher = more drought stress)
unit: kPa
dataset: MERRA-2
source: NASA POWER daily T2M·RH2M (MERRA-2 mean temperature and relative humidity)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Period mean of saturation vapor pressure (at mean temperature) × (1 − relative humidity/100)
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
keywords: [VPD, vapor pressure deficit, dry air, water stress, transpiration, leaf scorch, drought]
---

## Definition
For each day of the growing season, the difference (in kPa) between "the water vapor the air could hold at that temperature" and "the water vapor actually in the air", averaged over the season. The higher it is, the drier the air and the faster leaves lose water.

## Why it matters
Even when there is water in the soil, if the air is too dry the vine closes its stomata (leaf pores), and photosynthesis and sugar accumulation stop. It is used for irrigation timing, investment in shading and misting (fine-spray cooling), and decisions on drought-tolerant varieties.

## How to read
- A positive slope means the air is getting drier. Many days above roughly 1.5 kPa mean high water stress.

## Caveats
- It is calculated from daily mean temperature and humidity, so it comes out lower than the actual midday VPD.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
