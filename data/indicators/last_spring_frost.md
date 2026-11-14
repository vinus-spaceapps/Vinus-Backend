---
id: last_spring_frost
name: Last spring frost
category: temp_frost
order: 70
short: Date of the last frost of spring (minimum temperature 0°C or below), counted as days from January 1 (Southern Hemisphere from July 1)
unit: day of year
dataset: MERRA-2
source: NASA POWER daily T2M_MIN (MERRA-2 2 m minimum temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Jan–Jun (Southern Hemisphere Jul–Dec)
condition: last day with daily minimum temperature ≤ threshold
threshold: 0
threshold_unit: °C
threshold_options: [0, -2]
aggregation: mean
robust: false
higher_is: worse
station_var: tmin
keywords: [late frost, last frost, spring frost, frost date, budburst, shoots, frost risk, end of frost]
---

## Definition
The last day between January and June (Southern Hemisphere: July–December) when the daily minimum temperature was at or below the threshold, given as a day of year with January 1 = 1 (Southern Hemisphere: July 1 = 1). Example: 100 = around April 10.

## Why it matters
If the last frost comes after budburst, young shoots risk freezing. Read together with the budburst date (green-up), it shows whether "frost is ending earlier, but buds are breaking even earlier", which informs frost-protection investment.

## How to read
- A negative slope means the last frost is coming earlier. If budburst moves earlier even faster, frost risk actually goes up.

## Caveats
- Years with no frost have no value. Regions where frost is rare (Barossa) may not have enough years to analyze.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
