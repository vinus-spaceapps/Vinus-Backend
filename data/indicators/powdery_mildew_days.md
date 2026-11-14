---
id: powdery_mildew_days
name: Powdery mildew risk days
category: disease
order: 20
short: Number of days in the growing season with a mean temperature of 21–30°C, when powdery mildew grows best
unit: days
dataset: MERRA-2
source: NASA POWER daily T2M, T2M_MAX (MERRA-2 mean and maximum temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: 21°C ≤ daily mean temperature ≤ 30°C and daily maximum temperature < 35°C
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
station_var: tmean
keywords: [powdery mildew, oidium, mildew, disease, spraying, sulfur, fungicide]
---

## Definition
The number of days in the growing season when the daily mean temperature was 21–30°C and the maximum temperature stayed below 35°C. It is a simplified, day-by-day version of the temperature condition in the Gubler-Thomas powdery mildew risk index.

## Why it matters
Powdery mildew spreads whenever it is warm, even without rain, so it takes a large share of spray costs even in dry regions. Used to set spray intervals and to choose disease-resistant varieties.

## How to read
- A positive slope (upward trend) means more days that favor powdery mildew. Heat waves above 35°C actually kill the fungus, so those days are not counted.

## Caveats
- The original index is calculated by the hour (6 or more hours in a day), so using daily means is an approximation.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
