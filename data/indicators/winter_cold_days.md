---
id: winter_cold_days
name: Winter severe cold days
category: temp_frost
order: 120
short: Number of winter days when the minimum temperature fell to or below the threshold (default −10°C)
unit: days
dataset: MERRA-2
source: NASA POWER daily T2M_MIN (MERRA-2 2 m minimum temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Winter (Dec–Feb; Southern Hemisphere Jun–Aug)
condition: daily minimum temperature ≤ threshold
threshold: -10
threshold_unit: °C
threshold_options: [-5, -10, -15, -20]
aggregation: count
robust: false
higher_is: worse
station_var: tmin
keywords: [cold wave, severe cold, extreme cold, winter freeze damage, winterkill, winter buds, dormancy, hard freeze]
---

## Definition
The number of winter days (Northern Hemisphere December of the previous year to February, Southern Hemisphere June–August) when the daily minimum temperature was at or below the threshold. The default is −10°C; you can switch to −5, −15 or −20°C.

## Why it matters
If winter minimum temperature is "the single coldest day", this is "how many cold days there were". Frequent cold waves add up damage to winter buds and trunks, so this is used for winter protection such as hilling up (mounding soil over the base of the vine) and windbreaks, and for choosing cold-hardy varieties.

## How to read
- A negative slope means cold waves are becoming fewer.
- Grapevine winter buds are generally badly damaged below about −15 to −20°C.

## Caveats
- In the Okanagan the grid comes out about 5°C colder than the weather station, so day counts may be heavily inflated.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
