---
id: winter_min_temp
name: Winter minimum temperature
category: temp_frost
order: 100
short: The minimum temperature on the coldest day of winter (Dec–Feb; Southern Hemisphere Jun–Aug)
unit: °C
dataset: MERRA-2
source: NASA POWER daily T2M_MIN (MERRA-2 2 m minimum temperature)
start_year: 2002
resolution: ~50 km (one MERRA-2 grid cell)
stage: Winter (Dec–Feb; Southern Hemisphere Jun–Aug)
stage_from: harvest
stage_to: budburst
condition: (no condition) minimum over the period
threshold:
threshold_unit:
threshold_options: []
aggregation: min
robust: false
higher_is: better
station_var: tmin
keywords: [winter, winter freeze, freeze damage, extreme cold, cold wave, winterkill, vine death, dormancy, winter cold, cold]
---

## Definition
The lowest daily minimum temperature of that winter (Northern Hemisphere December of the previous year to February, Southern Hemisphere June–August). For each year, it sums up "the coldest moment of that winter" in a single number.

## Why it matters
Even while dormant, grapevines' buds (winter buds) and trunks freeze to death when temperatures drop below −15 to −20°C. The January 2024 cold snap in the Okanagan, Canada, wiped out most of the following harvest. Used when weighing cold-hardy varieties and rootstocks, and investment in winter protection such as hilling up (mounding soil over the base of the vine).

## How to read
- A positive slope means the winter minimum is rising and the risk of extreme cold is falling.
- Even as averages warm, an extreme cold snap can still hit in any single year. Look at the extreme years too.

## Caveats
- The first season (2001) has no data for the previous December, so calculation starts in 2002.
- In the Okanagan, the grid minimum temperature comes out about 5°C lower than at the nearby weather station. Focus on the direction of change rather than the absolute value.

## References
- Team data workbook — sheets: region coordinates, indicators by year
- NASA POWER — https://power.larc.nasa.gov/
