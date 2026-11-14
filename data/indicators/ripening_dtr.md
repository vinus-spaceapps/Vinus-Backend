---
id: ripening_dtr
name: Harvest-period diurnal temperature range
category: growth
order: 160
short: Average difference between the daily maximum and minimum temperature over the last two months of ripening (Aug–Sep; Southern Hemisphere Feb–Mar)
unit: °C
dataset: MERRA-2
source: NASA POWER daily T2M_MAX, T2M_MIN (MERRA-2 2 m maximum and minimum temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: (no condition) period mean of (maximum temperature − minimum temperature)
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: better
station_var: tmean
keywords: [diurnal temperature range, day-night difference, harvest, ripening, color, aroma, acidity, anthocyanins]
---

## Definition
Each day's (maximum temperature − minimum temperature), averaged over the harvest period (Aug–Sep in the Northern Hemisphere, Feb–Mar in the Southern Hemisphere).

## Why it matters
A large diurnal temperature range (day–night temperature difference) during ripening protects red wine color (anthocyanins, the red pigments), aroma and acidity. It is more directly tied to quality than the whole-season range, so it is used for choosing varieties and sites and for harvest timing.

## How to read
- A negative slope (downward trend) means nights during ripening are getting relatively warmer. Read it together with the cool night index.

## Caveats
- With a 50 km grid, values come out smaller than the actual diurnal range in valleys and on hillsides.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
