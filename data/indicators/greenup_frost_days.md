---
id: greenup_frost_days
name: Frost days after green-up
category: temp_frost
order: 20
short: Number of days with a minimum temperature at or below the threshold in the 30 days after that year's satellite-observed budburst date (green-up)
unit: days
dataset: MERRA-2
source: NASA POWER daily T2M_MIN (MERRA-2) + MODIS MCD12Q2 green-up date
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: 30 days from that year's green-up date
condition: daily minimum temperature ≤ threshold
threshold: 0
threshold_unit: °C
threshold_options: [0, -2]
aggregation: count
robust: false
higher_is: worse
station_var: tmin
keywords: [green-up, frost after budburst, post-budburst frost, late frost, spring frost, shoots, freeze damage, frost damage]
---

## Definition
The number of days with a daily minimum temperature at or below the threshold (default 0°C) during the 30 days starting from that year's budburst date (green-up, the date the MODIS satellite sees vegetation turning green). Unlike the calendar-fixed "Frost days after budburst", the window moves with the budburst date, which changes from year to year.

## Why it matters
When warming makes buds break earlier, frost on the calendar may decline while frost "after budburst" stays the same or even increases. Because it looks at the frost new shoots are actually exposed to, it is more directly useful for frost-protection and insurance decisions.

## How to read
- A positive slope means new shoots are being hit by frost on more days.
- If it moves in a different direction from the calendar-fixed "Frost days after budburst", the difference is the effect of the shifting budburst date.

## Caveats
- Green-up reflects all vegetation in the region area, not just vineyards.
- In the Southern Hemisphere (Barossa), green-up picks up winter pasture, so it is not calculated.
- Years without a MODIS green-up date (such as 2026) are left out.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
