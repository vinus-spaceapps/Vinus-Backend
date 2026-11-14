---
id: harvest_hot_days
name: Hot days at harvest
category: heat
order: 70
short: Number of days in the harvest period (Aug–Sep) with a maximum temperature at or above the threshold (default 30°C)
unit: "days"
dataset: MERRA-2
source: NASA POWER daily T2M_MAX
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: daily maximum temperature ≥ threshold
threshold: 30
threshold_unit: °C
threshold_options: [30, 32, 35]
aggregation: count
robust: false
higher_is: worse
station_var: tmax
keywords: [harvest heat, ripening heat, hot days at ripening, acidity, aroma, alcohol, sugar]
---

## Definition
The number of days during the harvest period with a daily maximum temperature at or above the threshold (default 30°C). You can switch to 32 or 35°C.

## Why it matters
Heat during ripening quickly strips away acidity and aroma while pushing up only the sugar, which gives high-alcohol, flat-tasting wines. Used when deciding whether to bring the harvest forward or add more shade.

## How to read
- A positive slope means more hot days during ripening.

## Caveats
- As a 50 km grid average, it does not reflect differences in elevation or slope.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
