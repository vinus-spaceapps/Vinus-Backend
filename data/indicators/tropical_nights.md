---
id: tropical_nights
name: Growing-season tropical nights
category: heat
order: 60
short: Number of growing-season days when even the night-time minimum temperature stayed at or above the threshold (default 20°C)
unit: days
dataset: MERRA-2
source: NASA POWER daily T2M_MIN (MERRA-2 2 m minimum temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: daily minimum temperature ≥ threshold
threshold: 20
threshold_unit: °C
threshold_options: [18, 20, 22]
aggregation: count
robust: false
higher_is: worse
station_var: tmin
keywords: [tropical nights, hot nights, warm nights, night heat, night temperature, acidity, aroma, respiration]
---

## Definition
The number of growing-season days with a daily minimum temperature at or above the threshold (default 20°C), meaning it stayed hot even at night. You can switch to 18°C or 22°C.

## Why it matters
On hot nights the grapes burn off acid (malic acid) through overnight respiration, so acidity drops quickly and aromas weaken. Used when weighing a change of variety, adjusting harvest timing, or securing higher-elevation vineyard sites.

## How to read
- A positive slope means hot nights are increasing.
- Cool European regions are close to 0. This matters most in regions with sultry summers, such as Yeongdong.

## Caveats
- For regions where the grid minimum temperature has a known error, also check the comparison with nearby weather stations.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
