---
id: bedd
name: Biologically effective degree days (BEDD)
category: growth
order: 40
short: Like growing degree days, but heat above 19°C earns no extra credit — the sum of heat that actually goes into ripening
unit: °C·days
dataset: MERRA-2
source: NASA POWER daily T2M (MERRA-2 2 m mean temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Σ min(max(mean temperature − 10, 0), 9)  (simplified)
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: neutral
station_var: tmean
keywords: [growing degree days, GDD, BEDD, effective degree days, heat summation, ripening, heat, variety, sugar]
---

## Definition
Each day of the growing season adds (mean temperature − 10°C), but counts at most 9 per day. It is a simplified calculation of Gladstones' index, built on the idea that heat above a daily mean of 19°C adds nothing more to grape ripening.

## Why it matters
Standard growing degree days (GDD) give a lot of credit to hot days, which overstates ripening speed in hot regions. A widening gap between this indicator and standard GDD means more "heat that makes it hotter but doesn't help ripening", so it complements decisions on changing varieties.

## How to read
- Read it alongside standard GDD. If GDD is rising but BEDD rises less, most of the added heat is heat above 19°C.

## Caveats
- A simplified version that leaves out the latitude and diurnal temperature range (day–night temperature difference) adjustments of the original Gladstones index.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
- Gladstones, J. (1992), Viticulture and Environment. Winetitles
