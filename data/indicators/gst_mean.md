---
id: gst_mean
name: Growing-season mean temperature
category: growth
order: 20
short: Average of the daily mean temperature over the growing season — the most basic climate indicator for classifying the world's wine regions
unit: °C
dataset: MERRA-2
source: NASA POWER daily T2M (MERRA-2 2 m mean temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
station_var: tmean
keywords: [mean temperature, temperature, warm, warming, climate zone, variety, wine style, GST, rising temperature]
---

## Definition
The average of the daily mean temperature over the growing season (Apr 1–Oct 31 in the Northern Hemisphere, Oct 1–Apr 30 in the Southern Hemisphere). It is the most widely used benchmark for classifying regions in wine climate research (Growing Season Temperature).

## Why it matters
It is the simplest way to show what style of wine a region produces. As it rises, you can check whether your current varieties are moving out of their suitable range for the region, so it is used for planning variety changes.

## How to read
- A positive slope (upward trend) means the region is shifting into a warmer climate zone.
- Bands (approximate): 13–15°C cool (Riesling, Pinot Noir), 15–17°C intermediate (Chardonnay, Merlot), 17–19°C warm (Cabernet Sauvignon, Syrah), 19–21°C hot (Grenache, Zinfandel).

## Caveats
- Because it is a 50 km grid average, differences in elevation and hillside position are not captured.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
- Jones, G. V. et al. (2005), Climate change and global wine quality — https://doi.org/10.1007/s10584-005-4704-2
