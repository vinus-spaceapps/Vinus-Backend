---
id: water_balance_summer
name: Summer water balance
category: drought
order: 20
short: Rain over two summer months (Jul–Aug) minus the water lost to evaporation. Water shortage around veraison
unit: "mm"
dataset: MERRA-2
source: NASA POWER daily T2M·T2M_MAX·T2M_MIN·PRECTOTCORR
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Summer (Jul–Aug; Southern Hemisphere Jan–Feb)
condition: Σ (precipitation − reference evapotranspiration ET0), Hargreaves equation
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: better
keywords: [summer drought, water balance, water stress, water deficit, irrigation, veraison]
---

## Definition
The sum of daily (precipitation − reference evapotranspiration) over the two summer months (July–August; Southern Hemisphere January–February).

## Why it matters
A moderate water shortage around veraison (when the berries soften and change color) improves quality, but if it is too severe, leaves drop and ripening stops. It is the most direct guide for deciding whether to irrigate at this stage.

## How to read
- A negative slope means the summer water shortage is getting worse.

## Caveats
- The Hargreaves equation tends to overestimate evapotranspiration in humid places.
- Computed directly by the team from the raw daily data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: computed from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
