---
id: frost_after_budburst
name: Frost days after budburst
category: temp_frost
order: 10
short: Number of days in the budburst season (Apr–May; Southern Hemisphere Oct–Nov) when the minimum temperature fell to or below the threshold
unit: days
dataset: MERRA-2
source: NASA POWER daily T2M_MIN (MERRA-2 2 m minimum temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Spring (Apr 1–May 31; Southern Hemisphere Oct 1–Nov 30)
stage_from: budburst
stage_to: flowering
condition: daily minimum temperature ≤ threshold
threshold: 0
threshold_unit: °C
threshold_options: [0, -1, -2, -3]
aggregation: count
robust: false
higher_is: worse
station_var: tmin
keywords: [frost, spring frost, late frost, budburst, shoots, freeze damage, frost damage, below freezing, green-up, cold injury]
---

## Definition
The number of days in spring, when buds break and new shoots grow (Northern Hemisphere April 1–May 31, Southern Hemisphere October 1–November 30), when the daily minimum temperature was at or below the threshold. The default is 0°C or below; you can switch to −1°C, −2°C (hard frost) or −3°C.

## Why it matters
Once buds have broken, young shoots freeze easily below 0°C, which can sharply cut that year's harvest (France 2021, South Australia 2024). Use it to check "are these days becoming more common in our region?" when weighing frost-protection equipment such as frost fans or sprinklers, or frost insurance.

## How to read
- A positive slope means frost risk after budburst is rising; a negative slope means it is falling.
- Even if frost itself becomes rarer with warming, frost "after budburst" may not decline if buds also break earlier. Check the budburst date (green-up) indicator as well.
- Frost damage tends to cluster in a few years, so many years are 0. Even if the trend is not significant, look at the extreme years too.

## Caveats
- MERRA-2 uses a grid of about 50 km, so it does not capture cold-air pools on valley floors well. Within the same grid cell, 1 km night-time land surface temperatures differ by 3–6°C on average (based on a MODIS comparison).
- The minimum-temperature error compared with nearby weather stations differs by region. In the Okanagan the grid runs about 5°C colder than the station, so frost days may come out high.
- At the planning stage this was defined as "60 days after green-up", but the team's aggregated values are calculated over a fixed April–May window (all 156 values checked against the daily data). To see the effect of budburst dates shifting from year to year, use the budburst date (green-up) indicator separately.
- The −1°C and −3°C thresholds were calculated directly from the daily data using the same definition.

## References
- Team data workbook — sheets: wine indicator data, indicators by year, station error
- Gelaro et al. (2017), MERRA-2 — https://doi.org/10.1175/JCLI-D-16-0758.1
- NASA POWER — https://power.larc.nasa.gov/
