---
id: downy_mildew_days
name: Downy mildew infection risk days
category: disease
order: 10
short: Number of days in the early growing season (Apr–Jun) with a mean temperature of 10°C or more and at least 10 mm of rain, when primary downy mildew infection is likely
unit: days
dataset: MERRA-2
source: NASA POWER daily T2M, PRECTOTCORR (MERRA-2 mean temperature and precipitation)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Early growing season (Apr–Jun; Southern Hemisphere Oct–Dec)
condition: Daily mean temperature ≥ 10°C and daily precipitation ≥ 10 mm  (simplified 3-10 rule)
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [downy mildew, mildew, disease, spraying, fungicide, infection, 3-10 rule, rain]
---

## Definition
The number of days in the early growing season (Apr–Jun in the Northern Hemisphere, Oct–Dec in the Southern Hemisphere) when the daily mean temperature was 10°C or higher and at least 10 mm of rain fell. It is a simplified, weather-only version of the "3-10 rule" (three 10s: shoots 10 cm long, temperature 10°C, rain 10 mm), which describes the conditions for primary downy mildew infection in grapevines.

## Why it matters
Downy mildew is a major vine disease that shrivels leaves and bunches and can ruin a whole season. More primary-infection risk days mean the first spray has to come earlier and sprays have to be more frequent, so this is used for spray planning and for deciding on disease-resistant varieties.

## How to read
- A positive slope (upward trend) means more days that favor the start of downy mildew.

## Caveats
- The shoot-length condition is not included. Actual infection depends heavily on how long the leaves stay wet.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
