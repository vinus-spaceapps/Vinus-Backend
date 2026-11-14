---
id: harvest_aerosol_days
name: Harvest-period smoke aerosol days
category: smoke_air
order: 20
short: Number of days from veraison to harvest when the UV aerosol index (smoke, dust) was at or above the threshold
unit: days
dataset: OMI
source: OMI/Aura OMAERUVd UV Aerosol Index
start_year: 2005
resolution: 1° grid (sensor pixels a few tens of km across)
stage: Veraison to harvest
stage_from: veraison
stage_to: harvest
condition: UV aerosol index ≥ threshold
threshold: 1.0
threshold_unit: (index)
threshold_options: [0.7, 1.0, 1.5]
aggregation: count
robust: true
higher_is: worse
keywords: [aerosol, smoke, dust, fine dust, yellow dust, haze, wildfire, sky, air quality]
---

## Definition
The number of days from veraison (when the grapes start to change color) to harvest day when the satellite-measured UV aerosol index was at or above the threshold (default 1.0). The index rises as smoke and dust particles that absorb sunlight increase.

## Why it matters
Read alongside carbon monoxide (harvest-period smoke exposure days), it lets you cross-check whether "smoke actually covered the sky". When both indicators move in the same direction, the case that smoke exposure is rising is stronger.

## How to read
- This indicator spikes, like wildfire smoke, so Sen's slope (a trend estimate that is less swayed by spike years) and the Mann-Kendall test (a check on whether the trend is statistically significant) are the default.
- Dust such as yellow dust (Asian dust) also raises the index, so in East Asian regions, read it separately from spring dust.

## Caveats
- Actual values have not been aggregated yet, so the screen shows sample data (a mockup).
- Since 2007, OMI has lost part of its sensor's field of view (the row anomaly), so it observes less often.
- On cloudy days values are missing, so the day count can come out too low.

## References
- Torres et al. (2007), Aerosols and surface UV products from OMI — https://doi.org/10.1029/2007JD008809
