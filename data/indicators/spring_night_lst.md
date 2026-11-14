---
id: spring_night_lst
name: Spring night land surface temperature (1 km)
category: temp_frost
order: 170
short: Average night-time ground surface temperature measured by the MODIS satellite at 1 km resolution during the spring frost-risk season
unit: °C
dataset: MODIS
source: MODIS Aqua night-time land surface temperature (MYD11 LST_Night_1km), 8-day periods, median of the 1 km pixels in the region area
start_year: 2003
resolution: 1 km (median of pixels within the ~11 km region area)
stage: Spring (frost-risk window)
stage_from: budburst
stage_to: flowering
condition: (no condition) period mean
threshold:
threshold_unit:
threshold_options: []
aggregation: mean
robust: false
higher_is: better
keywords: [night, night-time, land surface temperature, LST, satellite, 1 km, cold air, frost pocket, valley floor, MODIS]
---

## Definition
The night-time ground surface temperature measured at 1 km resolution by the MODIS satellite (Aqua, which passes over at about 1:30 a.m.) during the spring frost-risk season, taken as the median of the pixels in the region area and then averaged.

## Why it matters
The satellite directly sees night-time cold near the vineyards that a 50 km climate grid cannot show. Even within one region, night temperatures differ by 3–6°C on average between 1 km pixels, so this serves as supporting evidence for deciding where to put frost-protection equipment.

## How to read
- A positive slope means spring nights are getting warmer and frost risk is going down.
- Land surface temperature is a different physical quantity from 2 m air temperature, so focus on the direction of change rather than the absolute value.

## Caveats
- Cloudy nights have no value, so the average leans toward clear nights (clear nights are colder).
- The exact aggregation window (start and end of the spring period) follows the processing done by the team member in charge of MODIS and must be confirmed before the presentation.

## References
- Team data workbook — sheets: MODIS summary, MODIS by year
- Wan, Z. (2014), collection-6 MODIS LST — https://doi.org/10.1016/j.rse.2013.08.027
