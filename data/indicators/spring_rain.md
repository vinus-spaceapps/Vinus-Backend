---
id: spring_rain
name: Spring rainfall
category: rain_water
order: 80
short: Total rain in spring (Apr–May; Southern Hemisphere Oct–Nov)
unit: "mm"
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Spring (Apr 1–May 31; Southern Hemisphere Oct 1–Nov 30)
condition: (no condition) total over the period
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: neutral
keywords: [spring rain, spring rainfall, downy mildew, new shoots, early growth, budburst, first spray]
---

## Definition
The total rain that fell over the two spring months.

## Why it matters
Heavy rain in spring, when new shoots are growing, gets downy mildew started early; too little slows early growth. It is used to time the first spray and to decide on early irrigation.

## How to read
- Year-to-year variation is large, so look at the extreme years as well.

## Caveats
- MERRA-2 precipitation is model output corrected with observations, so it can underestimate local rain.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
