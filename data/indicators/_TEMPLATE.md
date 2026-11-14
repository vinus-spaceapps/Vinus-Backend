---
# Indicator md template — the variable team copies this file to create a new indicator.
# Name the file after its id: data/indicators/<id>.md  (files starting with an underscore are not read)
id: example_indicator            # lowercase letters and underscores. The frontend, AI and CSV paths all use this value.
name: Example indicator           # card title (in growers' words)
category: temp_frost             # temp_frost (temperature & frost) | rain_water (rain & water) | smoke_air (smoke & air) | growth (growth)
order: 99                         # card display order (lower comes first; 10s·20s·30s·40s within each category)
short: One-line definition        # first line of the hover text; the definition the variable-picker AI reads
unit: days                        # graph axis unit
dataset: MERRA-2                  # MERRA-2 | GPM IMERG | GLDAS | AIRS | OMI | MODIS
source: MERRA-2 M2SDNXSLV T2MMIN (2 m daily minimum temperature)
start_year: 1981                  # first complete season available from this dataset
resolution: ~50 km
stage: Budburst to flowering      # aggregation period (growth stage)
stage_from: budburst              # budburst | flowering | veraison | harvest | harvest_minus_21
stage_to: flowering
condition: Daily minimum temperature < threshold    # human-readable condition
threshold: 0                      # threshold value (leave empty if there is no condition)
threshold_unit: °C
threshold_options: [0, -1, -2]    # thresholds the analysis screen and the insight AI can switch between
aggregation: count                # count (number of days) | sum (total) | mean (average)
robust: false                     # if true, the headline slope uses Sen's slope; use for spiky indicators (smoke, etc.)
higher_is: worse                  # worse | better | neutral  (is a higher value bad for growers?)
keywords: [example, keyword]      # fallback search words for the variable-picker AI
---

## Definition
Describe the indicator in growers' words, in 2–3 sentences.

## Why it matters
Which decisions it informs (changing varieties, investing in frost protection, insurance and contracts, harvest planning).

## How to read
What an increase or decrease means, and how to read the slope.

## Caveats
Resolution, missing data, breaks in the data record, etc.

## References
- Source title — URL
