---
id: gs_rh_mean
name: Growing-season mean humidity
category: disease
order: 70
short: Average of the daily mean relative humidity over the growing season
unit: "%"
dataset: MERRA-2
source: NASA POWER daily RH2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
keywords: [humidity, relative humidity, damp, disease, mildew, fungus, spraying]
---

## Definition
The average of the daily mean relative humidity over the growing season.

## Why it matters
The more humid a region, the more it costs to control fungal diseases. Whether humidity is rising or falling informs spray planning and decisions on disease-resistant varieties.

## How to read
- A positive slope (upward trend) means the growing season is getting damper.

## Caveats
- An approximation based on daily mean values.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
