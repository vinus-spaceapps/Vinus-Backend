---
id: huglin_index
name: Huglin index
category: growth
order: 30
short: A heat index for gauging which grape varieties can ripen (based on mean and maximum temperature, with a latitude adjustment)
unit: index
dataset: MERRA-2
source: NASA POWER daily T2M, T2M_MAX (MERRA-2 2 m mean and maximum temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Apr 1–Sep 30 (Southern Hemisphere Oct 1–Mar 31)
stage_from: budburst
stage_to: harvest
condition: Σ [(mean temperature − 10) + (maximum temperature − 10)] / 2 × latitude coefficient
threshold:
threshold_unit:
threshold_options: []
aggregation: sum
robust: false
higher_is: neutral
station_var: tmean
keywords: [Huglin, Huglin index, variety, variety change, replanting, suitability, heat, climate zone, Cabernet, Pinot]
---

## Definition
For each day from April 1 to September 30 (Southern Hemisphere October 1 to March 31), [(mean temperature − 10) + (maximum temperature − 10)] ÷ 2 is added up, and the total is multiplied by a latitude coefficient that gives a little extra credit to higher latitudes, where summer days are longer.

## Why it matters
Each variety needs a roughly known Huglin index to ripen (e.g., Pinot Noir and Riesling about 1700, Merlot and Cabernet Sauvignon about 1900, Syrah and Grenache about 2100). When considering a variety change, it shows "which variety band our region is moving into".

## How to read
- A positive slope (upward trend) means the region is moving into a warmer variety band.
- Index classes: below 1500 very cool, 1500–1800 cool, 1800–2100 temperate, 2100–2400 warm, 2400 and above hot.

## Caveats
- Because it uses maximum temperature, any error in maximum temperature compared with weather stations (about +2°C at Barossa, for example) carries straight into the index.

## References
- Team data workbook: sheets 2 (wine indicator data) and 7 (indicators by year)
- Huglin, P. (1978), Nouveau mode d'évaluation des possibilités héliothermiques d'un milieu viticole
- Tonietto & Carbonneau (2004), A multicriteria climatic classification system for grape-growing regions — https://doi.org/10.1016/j.agrformet.2003.06.001
