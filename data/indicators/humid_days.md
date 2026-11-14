---
id: humid_days
name: Growing-season humid days
category: disease
order: 40
short: Number of days in the growing season with humidity of 80% or more and temperatures of 15–25°C, when fungal diseases spread easily
unit: days
dataset: MERRA-2
source: NASA POWER daily RH2M, T2M (MERRA-2 2 m relative humidity and mean temperature)
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
stage_from: budburst
stage_to: harvest
condition: Daily mean relative humidity ≥ 80% and 15°C ≤ daily mean temperature ≤ 25°C
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [humidity, mildew, downy mildew, powdery mildew, disease, spraying, fungicide, damp, fungus, disease pressure]
---

## Definition
The number of days in the growing season when the daily mean relative humidity was 80% or higher and the daily mean temperature was 15–25°C. These conditions favor fungal diseases such as downy mildew and powdery mildew.

## Why it matters
Fungal diseases are among the biggest drivers of spray costs and yield loss. Used to plan the number of sprays, consider disease-resistant varieties, and decide on converting to organic.

## How to read
- A positive slope (upward trend) means more days that favor disease.
- Dry regions (Napa, Barossa) sit close to 0. The indicator matters most in humid regions (Yeongdong, Bordeaux).

## Caveats
- Based on daily mean humidity, so nighttime dew and hour-by-hour humidity are not captured. It is simpler than real disease-forecasting models.

## References
- Team data workbook: sheets 2 (wine indicator data) and 7 (indicators by year)
- NASA POWER — https://power.larc.nasa.gov/
