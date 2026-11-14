---
id: hot_humid_days
name: Hot and humid days
category: disease
order: 50
short: Number of sultry days in the growing season with a mean temperature of 25°C or more and humidity of 70% or more
unit: "days"
dataset: MERRA-2
source: NASA POWER daily T2M, RH2M
start_year: 2001
resolution: ~50 km (one MERRA-2 grid cell)
stage: Growing season (Apr 1–Oct 31; Southern Hemisphere Oct 1–Apr 30)
condition: Daily mean temperature ≥ 25°C and relative humidity ≥ 70%
threshold:
threshold_unit:
threshold_options: []
aggregation: count
robust: false
higher_is: worse
keywords: [hot and humid, muggy, sultry, sour rot, ripe rot, anthracnose, rainy season, monsoon, disease]
---

## Definition
The number of days in the growing season when the daily mean temperature was 25°C or higher and relative humidity was 70% or higher.

## Why it matters
Hot, humid weather spreads warm-weather diseases such as sour rot and ripe rot (anthracnose), and berries are easily damaged. Used for spray planning in regions like Yeongdong, where the summer rainy season (monsoon) is hot.

## How to read
- A positive slope (upward trend) means more sultry days.

## Caveats
- An approximation based on daily mean values.
- Calculated directly from the team's daily raw data (DERIVED in scripts/import_team_xlsx.py).

## References
- Team data workbook: calculated from the D_ daily raw data
- NASA POWER — https://power.larc.nasa.gov/
