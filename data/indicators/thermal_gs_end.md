---
id: thermal_gs_end
name: Growing season end date (temperature-based)
category: growth
order: 210
short: First day of the first 5-day run with a mean temperature below 10°C after August — the thermal end of the growing season
unit: "day of year"
dataset: MERRA-2
source: NASA POWER daily T2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Aug–Dec (Southern Hemisphere Feb–Jul)
condition: First day of 5 consecutive days with mean temperature < 10°C
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [end of growing season, autumn, fall, late autumn, late-ripening varieties, temperature]
---

## Definition
After August 1 (Southern Hemisphere February 1), the first day of the first run of 5 consecutive days with a daily mean temperature below 10°C.

## Why it matters
If this date comes later, even late-ripening varieties get enough warm days to ripen fully, but cane maturing (cane lignification, when green shoots turn woody) is delayed too. Used to decide on planting late-ripening varieties and on winter preparation.

## How to read
- A positive slope (upward trend) means the growing season is ending later.

## Caveats
- The most recent year may be missing if that year's autumn is not over yet.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
