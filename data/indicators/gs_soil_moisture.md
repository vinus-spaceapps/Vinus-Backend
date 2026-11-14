---
id: gs_soil_moisture
name: Root-zone soil moisture (growing season)
category: drought
order: 100
short: Average wetness of the soil at root depth during the growing season (0 = dry, 1 = saturated)
unit: 0–1
dataset: MERRA-2
source: NASA POWER daily GWETROOT (MERRA-2 root-zone soil wetness)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
stage_from: budburst
stage_to: harvest
condition: (no condition) mean over the period
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: better
keywords: [drought, soil moisture, dry soil, soil, water shortage, irrigation, watering, root zone]
---

## Definition
How wet the soil is at the depth where roots spread (the root zone), expressed as a value from 0 (completely dry) to 1 (full of water) and averaged over the growing season.

## Why it matters
Vines produce good grapes under moderate water stress, but if the soil gets too dry, leaves drop and sugar accumulation stops. It is used for irrigation investment, switching rootstocks, and considering drought-tolerant varieties.

## How to read
- A negative slope means growing-season soil is gradually drying out.
- Even if rain increases, soil moisture can fall if rising temperatures increase evaporation.

## Caveats
- These are model values and differ from the actual soil moisture in an irrigated vineyard.
- We plan to cross-check with GLDAS Noah 2.1 (~25 km).

## References
- Team data workbook — sheet "7_Indicators by year"
- NASA POWER — https://power.larc.nasa.gov/
