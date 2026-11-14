---
id: water_balance
name: Growing-season water balance
category: drought
order: 10
short: Growing-season rain minus the water lost by evaporation from soil and leaves. The more negative, the bigger the water shortage
unit: mm
dataset: MERRA-2
source: NASA POWER daily T2M·T2M_MAX·T2M_MIN·PRECTOTCORR (MERRA-2)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Σ (precipitation − reference evapotranspiration ET0), with ET0 from the Hargreaves equation (FAO-56)
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: better
keywords: [water balance, water deficit, evapotranspiration, drought, water shortage, irrigation, dryness index, ET0]
---

## Definition
The sum of daily (precipitation − reference evapotranspiration) over the growing season. Reference evapotranspiration (ET0) uses the Hargreaves equation (FAO-56), calculated from temperature and latitude. A negative value means more water is lost to evaporation than falls as rain.

## Why it matters
Rainfall alone misses the effect of rising temperatures increasing evaporation. Water balance shows "how short of water the vineyard actually is", making it the most direct guide for sizing irrigation, securing water, and choosing drought-tolerant rootstocks.

## How to read
- A negative slope means the water shortage is getting worse.
- It is similar in idea to the wine-region Dryness Index (Riou), but it is a simplified version that leaves out water stored in the soil.

## Caveats
- The Hargreaves equation tends to overestimate evapotranspiration in humid places and underestimate it in windy places.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
