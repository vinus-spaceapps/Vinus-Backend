---
id: spring_wet_days
name: Rainy days in spring
category: rain_water
order: 90
short: Number of days with rain (1 mm or more) in spring (Apr–May)
unit: "days"
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Spring (Apr 1–May 31; Southern Hemisphere Oct 1–Nov 30)
condition: Daily precipitation ≥ 1 mm
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [spring rain, rainy days, downy mildew, anthracnose, spraying, disease, new shoots]
---

## Definition
The number of days over the two spring months with 1 mm or more of rain.

## Why it matters
When new shoots and young leaves get wet often, downy mildew and anthracnose get started. For disease, how "often" it rains matters more than how much, so this is used to schedule the first sprays.

## How to read
- A positive slope means spring rain is becoming more frequent.

## Caveats
- Model precipitation tends to produce light rain more often than actually occurs.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
