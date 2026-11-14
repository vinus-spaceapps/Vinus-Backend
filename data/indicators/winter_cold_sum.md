---
id: winter_cold_sum
name: Winter cold accumulation
category: temp_frost
order: 130
short: Sum of how far the minimum temperature fell below −10°C over the winter; the total amount of severe cold
unit: "°C·days"
dataset: MERRA-2
source: NASA POWER daily T2M_MIN
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Winter (Dec–Feb; Southern Hemisphere Jun–Aug)
condition: Σ max(0, −10°C − daily minimum temperature)
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: worse
station_var: tmin
keywords: [cold wave, cold accumulation, severe cold, extreme cold, cumulative cold, freeze damage, winter damage]
---

## Definition
The sum, over every winter day, of how many degrees colder than −10°C it was (e.g., a day at −14°C counts as 4).

## Why it matters
If winter severe cold days tell you "how many times", this tells you "how deep and how long". Damage to winter buds and trunks scales with how deep and how long the cold is, so this informs the choice of cold-hardy varieties and rootstocks.

## How to read
- A negative slope means the total amount of severe cold is shrinking.

## Caveats
- In the Okanagan, grid temperatures run about 5°C colder than the weather station, so cold indicators may be inflated.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data sheets
- NASA POWER — https://power.larc.nasa.gov/
