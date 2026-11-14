---
id: harvest_dry_spell
name: Longest dry spell at harvest
category: drought
order: 90
short: Longest run of consecutive days without rain during the harvest period (Aug–Sep)
unit: "days"
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Harvest period (Aug–Sep; Southern Hemisphere Feb–Mar)
condition: Longest run of consecutive days with daily precipitation < 1 mm
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: neutral
keywords: [dry harvest, clear weather, sunny, dry spell, no rain, harvest schedule, shriveling]
---

## Definition
The longest run of consecutive harvest-period days with less than 1 mm of daily rain.

## Why it matters
A long stretch of clear weather at harvest keeps bunches dry and lets them ripen healthily, which is good for quality; but if it lasts too long, berries can shrivel. It is used for harvest scheduling and decisions on irrigation just before harvest.

## How to read
- A positive slope means harvest is getting drier (usually good for quality).

## Caveats
- In regions with almost no rain (Napa), the value is always long.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
