---
id: radiation_frost_nights
name: Radiation frost nights
category: temp_frost
order: 40
short: Number of spring nights with light wind (under 2 m/s) and a minimum temperature of 2°C or below, when the ground cools off and frost settles easily
unit: days
dataset: MERRA-2
source: NASA POWER daily T2M_MIN and WS2M (MERRA-2 2 m minimum temperature and wind speed)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Spring (Apr 1–May 31; Southern Hemisphere Oct 1–Nov 30)
condition: daily minimum temperature ≤ 2°C and daily mean wind speed < 2 m/s
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
station_var: tmin
keywords: [radiation frost, calm night, clear night, still night, cold air, frost fan, wind machine, frost risk]
---

## Definition
The number of spring days (Northern Hemisphere April–May, Southern Hemisphere October–November) when the daily minimum temperature was 2°C or below and the daily mean wind speed was under 2 m/s.

## Why it matters
On calm, clear nights the ground's heat escapes to the sky, cold air pools on valley floors and frost settles (radiation frost). Frost fans prevent frost on exactly these nights by mixing in the warmer air above, which makes this the most direct indicator for frost-fan investment decisions.

## How to read
- A positive slope means more nights that call for frost fans.
- Even when the grid minimum is 2°C, valley floors can be below freezing, which is why the threshold is set at 2°C.

## Caveats
- Because wind speed is a daily mean, it can miss nights when the wind died down overnight.
- Typical wind strength differs between regions, so night counts are hard to compare directly across regions.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
