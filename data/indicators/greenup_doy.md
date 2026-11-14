---
id: greenup_doy
name: Green-up date (leaf-out)
category: growth
order: 190
short: The day the satellite saw vegetation start turning green again that year (counted from January 1)
unit: day of year
dataset: MODIS
source: MODIS MCD12Q2 Land Cover Dynamics, Greenup (median of 500 m pixels over the wine region)
start_year: 2001
resolution: 500 m (median of pixels over the wine region)
stage: Once a year
stage_from: budburst
stage_to: budburst
condition: (no condition) one date per year
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: neutral
keywords: [budburst, budbreak, green-up, greenup, leaf-out, spring, start of season, earlier, phenology]
---

## Definition
The date when, as seen by the MODIS satellite, vegetation started turning green again that year, counted with January 1 as day 1 (e.g., 80 = late March). It is the median of the 500 m pixels covering the wine region.

## Why it matters
When buds break early, new shoots are exposed for longer to the late spring frosts that follow. It is the key to explaining "why frost damage hasn't gone away even though it has gotten warmer", and it is also the starting point for counting frost days after budburst.

## How to read
- A negative slope (downward trend) means green-up is coming earlier. Read it together with frost days after budburst.

## Caveats
- It reflects all vegetation in the wine region (including grass and forest), not just vineyards.
- In the Southern Hemisphere (Barossa), winter pasture greens up first, so the date may not match grapevine budburst (September).
- In years with a lot of cloud or snow, there are fewer valid pixels.

## References
- Team data workbook — sheet 8 (MODIS green-up)
- Friedl et al., MCD12Q2 v6.1 — https://doi.org/10.5067/MODIS/MCD12Q2.061
