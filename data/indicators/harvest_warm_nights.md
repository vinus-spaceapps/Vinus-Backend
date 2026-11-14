---
id: harvest_warm_nights
name: Warm nights at harvest
category: heat
order: 80
short: Number of days in the harvest period (Aug–Sep) when the night-time minimum temperature stayed warm, at or above the threshold (default 15°C)
unit: "days"
dataset: MERRA-2
source: NASA POWER daily T2M_MIN
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: daily minimum temperature ≥ threshold
threshold: 15
threshold_unit: °C
threshold_options: [12, 15, 18]
aggregation: count
robust: false
higher_is: worse
station_var: tmin
keywords: [warm nights, hot nights, tropical nights, harvest nights, ripening nights, acidity, color]
---

## Definition
The number of days during the harvest period with a daily minimum temperature at or above the threshold (default 15°C). You can switch to 12 or 18°C.

## Why it matters
When nights are warm during ripening, the grapes use up acid through respiration overnight and develop less color. Compared with the cool night index (September average), it shows "on how many nights" directly.

## How to read
- A positive slope means more warm nights during ripening.

## Caveats
- As a 50 km grid average, it does not reflect differences in elevation or slope.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
