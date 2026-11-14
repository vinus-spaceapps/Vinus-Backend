---
id: vpd_high_days
name: High-VPD days
category: drought
order: 60
short: Number of growing-season days when the air is very dry (VPD 1.5 kPa or more) and leaves lose water fast
unit: "days"
dataset: MERRA-2
source: NASA POWER daily T2M·RH2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Vapor pressure deficit (VPD) ≥ 1.5 kPa
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [VPD, high VPD, dry air, water stress, transpiration, stomata, misting]
---

## Definition
The number of growing-season days when the daily mean vapor pressure deficit (VPD) was 1.5 kPa or more.

## Why it matters
On high-VPD days, the vine closes its stomata (leaf pores) and photosynthesis stops, even if there is water in the soil. It is used for decisions on misting, shading and irrigation timing.

## How to read
- A positive slope means dry-air stress is becoming more frequent.

## Caveats
- An approximation based on daily mean values.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
