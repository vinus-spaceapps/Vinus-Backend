---
id: gdd_milestone_date
name: GDD milestone date
category: growth
order: 50
short: The date when growing degree days accumulated since the start of the growing season reach the threshold (default 1,000 °C·days) — shows how much earlier veraison and harvest have become
unit: "day of year"
dataset: MERRA-2
source: NASA POWER daily T2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: From the start of the growing season (Apr 1; Southern Hemisphere Oct 1)
condition: Day when growing degree days (base 10°C) reach the threshold
threshold: 1000
threshold_unit: °C·days
threshold_options: [800, 1000, 1200]
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [ripening, veraison, harvest date, earlier harvest, growing degree days, GDD, phenology]
---

## Definition
Starting April 1 (Southern Hemisphere October 1), each day's (mean temperature − 10°C) is added up; this is the date when the total first reaches the threshold (default 1,000), given as a day number counted from January 1 (Southern Hemisphere: from July 1). You can switch the threshold to 800 or 1,200.

## Why it matters
Grapes change color and ripen once the accumulated heat reaches a certain level. If this date moves earlier, ripening falls in the hotter part of midsummer and quality can suffer, so it is used for harvest timing plans and decisions on changing varieties.

## How to read
- A negative slope (downward trend) means the same amount of heat builds up faster, so ripening comes earlier.

## Caveats
- In cool regions (Okanagan), many years drop out because the threshold is not reached by late October.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
