---
id: harvest_smoke_days
name: Harvest-period smoke exposure days
category: smoke_air
order: 10
short: Number of days from veraison to harvest when carbon monoxide (a smoke indicator) exceeded its usual level by the threshold multiple
unit: days
dataset: AIRS
source: AIRS L3 daily total carbon monoxide (AIRS3STD CO_total_column), supplemented by MERRA-2 surface organic carbon
start_year: 2003
resolution: 1° (~100 km)
stage: Veraison to harvest
stage_from: veraison
stage_to: harvest
condition: Total carbon monoxide > 2003–2012 same-date mean × threshold multiple
threshold: 1.5
threshold_unit: ×
threshold_options: [1.3, 1.5, 2.0]
aggregation: count
robust: true
higher_is: worse
keywords: [smoke, wildfire, bushfire, smoke taint, smoke exposure, ash, soot, fire, contract rejection]
---

## Definition
The number of days from the day the grapes start to change color (veraison) to harvest day when the total carbon monoxide in the air was at least the threshold multiple (default 1.5×) above the region's usual level (the 2003–2012 average for the same date). Carbon monoxide is a typical gas that travels along with wildfire smoke.

## Why it matters
Grapes exposed to smoke after veraison can give wine an ashy, medicinal smell (smoke taint), and wineries sometimes reject contracted fruit. In the US West in 2020, some fruit was rejected without testing, simply because "there was smoke". Used when weighing contract terms, insurance and harvest plans.

## How to read
- Wildfire smoke spikes sharply in a few years, so Sen's slope (less swayed by spike years) and the Mann-Kendall test (a check on whether the trend is statistically significant) are the default.
- Even if the trend is significant, make sure a single year is not driving the result: also look at the result with the most extreme year removed.

## Caveats
- Actual values have not been aggregated yet, so the screen shows sample data (a mockup).
- AIRS uses a 1° grid, so values are averages over an area much larger than a single wine region.
- Carbon monoxide is a proxy for smoke; it does not tell you how much volatile phenols (the smoke compounds behind the taint) actually built up in the grapes.
- The data assimilated into MERRA-2 aerosols changed in the early 2000s, so long-term comparisons need checking.

## References
- Estimated losses of about US$600 million to wine producers from the 2020 US West wildfire smoke — project plan v2, problem definition table
- AIRS Science Team, AIRS3STD v7 — https://doi.org/10.5067/UO3Q64CTTS1U
