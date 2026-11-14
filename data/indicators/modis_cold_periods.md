---
id: modis_cold_periods
name: Cold periods (1 km)
category: temp_frost
order: 60
short: Number of 8-day periods in the spring frost season when the coldest 1 km patch of land in the region was below freezing (frost pockets spotted by satellite)
unit: "periods"
dataset: MODIS
source: MODIS Aqua night-time land surface temperature (8-day periods, coldest of the 1 km pixels in the region area)
start_year: 2001
resolution: 1 km (pixels within the ~11 km region area)
stage: Spring (frost-risk window)
condition: number of 8-day periods when the night-time land surface temperature of the coldest 1 km pixel ≤ 0°C
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [frost pocket, cold air, cold-air pooling, valley floor, 1 km, satellite, low-lying ground, MODIS]
---

## Definition
The number of 8-day periods during the spring frost-risk season when the night-time land surface temperature of the coldest 1 km pixel in the region area was 0°C or below.

## Why it matters
Even when the 50 km climate-grid average is above freezing, some ground, such as valley floors, drops below 0°C. It shows how often frost pockets form, which helps decide where to put frost fans and whether to avoid low-lying blocks.

## How to read
- A negative slope means frost pockets are forming less often.

## Caveats
- Cloudy periods have no data, so the count may come out lower than reality.
- The exact aggregation window follows the processing done by the team member in charge of MODIS and still needs to be confirmed.

## References
- Team data workbook — sheets: MODIS summary, MODIS by year
