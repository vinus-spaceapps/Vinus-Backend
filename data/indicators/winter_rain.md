---
id: winter_rain
name: Dormancy rainfall
category: rain_water
order: 180
short: Total rain during dormancy (Nov–Mar; Southern Hemisphere May–Sep). The rain that refills soil water for spring
unit: mm
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR (MERRA-2 observation-corrected precipitation)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Dormancy (Nov–Mar; Southern Hemisphere May–Sep)
condition: (no condition) total over the period
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: better
keywords: [winter rain, winter rainfall, soil water, water storage, drought, irrigation, soil moisture recharge]
---

## Definition
The total rain that fell during dormancy (Northern Hemisphere previous November to March; Southern Hemisphere May to September).

## Why it matters
Regions with dry summers (Napa, Barossa, Bordeaux) get through the year on soil water stored up from winter rain. When winter rain declines, irrigation is needed from spring onward, so this is used for decisions on irrigation infrastructure and securing water.

## How to read
- A negative slope means the soil is being refilled less. Look at it together with growing-season water balance.

## Caveats
- Snowfall is included, converted to its water equivalent.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
