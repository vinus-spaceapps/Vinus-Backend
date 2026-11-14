---
id: ripening_temp
name: Harvest-period mean temperature
category: growth
order: 120
short: Daily mean temperature over the last two months of ripening (Aug–Sep; Southern Hemisphere Feb–Mar)
unit: °C
dataset: MERRA-2
source: NASA POWER daily T2M (MERRA-2 2 m mean temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: worse
station_var: tmean
keywords: [harvest, ripening period, ripening, temperature, acidity, aroma, sugar, alcohol]
---

## Definition
The average of the daily mean temperature during the harvest period (Aug–Sep in the Northern Hemisphere, Feb–Mar in the Southern Hemisphere).

## Why it matters
A hot ripening period pushes sugar up fast but strips out acidity and aroma, which tends to give high-alcohol, flat wines. Used to decide whether to harvest earlier or to add more shade and irrigation.

## How to read
- A positive slope (upward trend) means the ripening period is getting hotter. Read it together with the cool night index (night temperatures).

## Caveats
- In years when harvest finishes before this period ends, it may not line up with the actual ripening period.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
