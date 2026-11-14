---
id: gs_wind_mean
name: Growing-season mean wind speed
category: sun_wind
order: 70
short: Average of the daily mean wind speed at 2 m above ground over the growing season
unit: "m/s"
dataset: MERRA-2
source: NASA POWER daily WS2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
keywords: [wind, wind speed, breeze, airflow, windbreak, frost fan, drying]
---

## Definition
The average of the daily mean wind speed at 2 m above ground over the growing season.

## Why it matters
A moderate breeze dries the leaves and reduces disease, but when the wind dies down, frost risk rises, and when it gets stronger, water loss and broken shoots increase. Used to decide on windbreaks and frost fans.

## How to read
- A negative slope (downward trend) means the wind is getting weaker, which raises the risk of radiation frost (frost on calm, clear nights) and disease.

## Caveats
- Because it is a 50 km grid average, wind corridors along valleys are not captured.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
