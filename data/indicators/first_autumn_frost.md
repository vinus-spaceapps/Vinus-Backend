---
id: first_autumn_frost
name: First autumn frost
category: temp_frost
order: 80
short: Date of the first frost of autumn (minimum temperature 0°C or below), counted as days from January 1
unit: day of year
dataset: MERRA-2
source: NASA POWER daily T2M_MIN (MERRA-2 2 m minimum temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Jul–Dec (Southern Hemisphere Jan–Jun)
condition: first day with daily minimum temperature ≤ threshold
threshold: 0
threshold_unit: °C
threshold_options: [0, -2]
aggregation: mean
robust: false
higher_is: better
station_var: tmin
keywords: [first frost, autumn frost, fall frost, early frost, frost before harvest, late-ripening varieties, ice wine, harvest timing]
---

## Definition
The first day between July and December (Southern Hemisphere: January–June) when the daily minimum temperature was at or below the threshold, given as a day of year (January 1 = 1). Example: 300 = around October 27.

## Why it matters
Late-ripening varieties must be picked before the first frost. A later first frost changes the options, such as late-ripening varieties or ice wine, so this informs variety and harvest planning.

## How to read
- A positive slope means the first frost is arriving later. Read it together with the frost-free period.

## Caveats
- The latest year, whose autumn is not yet over, and years with no frost are left out.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
