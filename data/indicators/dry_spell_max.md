---
id: dry_spell_max
name: Longest dry spell (growing season)
category: drought
order: 80
short: Longest run of consecutive growing-season days without rain (1 mm or more)
unit: days
dataset: MERRA-2
source: NASA POWER daily PRECTOTCORR (MERRA-2 observation-corrected precipitation)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Longest run of consecutive days with daily precipitation < 1 mm
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [drought, dry spell, no rain, dry, water shortage, irrigation, consecutive dry days, dry monsoon]
---

## Definition
The longest run of consecutive growing-season days with less than 1 mm of daily rain.

## Why it matters
Even with the same rainfall total, a long break in the rain puts vines under severe water stress. It is used to judge the need for irrigation and the drought tolerance of rootstocks and varieties.

## How to read
- A positive slope means dry spells are getting longer. Look at it together with root-zone soil moisture.

## Caveats
- In regions with almost rainless summers (Napa, Barossa), the value is always long, so changes may not show up clearly.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
