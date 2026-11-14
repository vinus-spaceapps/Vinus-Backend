---
id: thermal_gs_start
name: Growing season start date (temperature-based)
category: growth
order: 200
short: First day of the first 5-day run with a mean temperature of 10°C or above — the thermal spring when vines start growing (counted from January 1; Southern Hemisphere from July 1)
unit: "day of year"
dataset: MERRA-2
source: NASA POWER daily T2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Jan–Jul (Southern Hemisphere Jul–Dec)
condition: First day of 5 consecutive days with mean temperature ≥ 10°C
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [start of growing season, start of spring, budburst, temperature, earlier, spring warming]
---

## Definition
Counting from January 1 (Southern Hemisphere July 1), the first day of the first run of 5 consecutive days with a daily mean temperature of 10°C or above.

## Why it matters
Grapevines start growing at a mean temperature of around 10°C. If this date moves earlier, buds break sooner and exposure to late frost lasts longer, so it is used for frost protection and variety choice.

## How to read
- A negative slope (downward trend) means the growing season is starting earlier. Compare it with the satellite green-up date.

## Caveats
- It means little in warm regions that often exceed 10°C even in winter (Barossa).
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
