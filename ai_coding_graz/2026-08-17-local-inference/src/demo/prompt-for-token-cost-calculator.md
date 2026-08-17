# Token Cost Calculator

Create a web app to compute the costs per token of local LLM inference. This enables the user to compare the costs of running local models on different hardware platforms and models, and make an informed decision in which direction to go.

## Heading and introduction

The page starts with the heading "Local token cost calculator".

Below it, add an introductory paragraph quickly descrining the purpose of the app.

## Input fields

The user can provide the following input in a form:

- Initial Hardware cost: numeric, valid range: 0 or more; default: 3000, variable: initial_hardware_cost_in_eur
- Token per second: 0.01 or more, default: 15, variable: token_count_per_second
- Daily usage in hours: numeric, valid range: 0.01 to 24; default: 3; variable: usage_hours_per_workday
- Power consumption in Watt: numeric, valid range: 1 or more, default: 250; variable: power_consumption_in_w
- Cost of power in cent per kWh: 0 or more, default: 20; variable: cost_of_power_in_cent_per_kwh
- Years in use: numeric, valid range: 0.01 or more, default: 4; variable: years_in_use
- Work days per year: integer, 1 or more, default: 220; variable: work_days_per_year

## Output area

Below the form, the following result values are shown:

- Total cost of ownership in EUR
- Total number of tokens (in millions)
- Cost per million tokens in EUR 

The results are calculated when

1. the page loads.
2. the value in an input field changes

## Calculation

Here is a Python script as an example of how the input variables are used to compute the output:

```python
# Constants
_CENTS_PER_EUR = 100
_SECONDS_PER_HOUR = 3_600

# Input
initial_hardware_cost_in_eur = 3000
token_count_per_second = 15.0
usage_hours_per_workday = 3.0
power_consumption_in_w = 120
cost_of_power_in_cent_per_kwh = 20.0
years_in_use = 4.0
work_days_per_year = 220

# Calculation
cost_of_power_in_eur_per_wh = cost_of_power_in_cent_per_kwh / _CENTS_PER_EUR / 1_000
power_consumption_per_work_day_in_w = power_consumption_in_w / 1_000 * usage_hours_per_workday
cost_of_power_by_work_day_in_cent = power_consumption_per_work_day_in_w * cost_of_power_in_eur_per_wh * 24
total_work_days_of_usage = years_in_use * work_days_per_year
total_hours_of_usage = total_work_days_of_usage * usage_hours_per_workday
total_cost_of_power_in_eur = power_consumption_per_work_day_in_w * total_hours_of_usage * cost_of_power_in_cent_per_kwh / _CENTS_PER_EUR
total_cost_of_ownership_in_eur = initial_hardware_cost_in_eur + total_cost_of_power_in_eur
total_token_count = token_count_per_second * total_hours_of_usage * _SECONDS_PER_HOUR
cost_per_token_in_cent = total_cost_of_ownership_in_eur * _CENTS_PER_EUR / total_token_count
million_token_count = total_token_count / 1_000_000
cost_per_million_token_in_eur = total_cost_of_ownership_in_eur / million_token_count

# Output
print(f"Total cost of ownership in EUR: {total_cost_of_ownership_in_eur:.2f} EUR")
print(f"Total number of tokens: {total_token_count / 1_000_000:.2f} million")
print(f"Cost per million tokens: {cost_per_million_token_in_eur:.2f} EUR")
```

## Visual design and layout

The app is responsive, scaleable and works well both on desktop and mobile.

The visual design is straightforward and easy to read. No fancy effects.

Here is a sketch on how to group, label and lay out the input fields:

```
Hardware

  Initial cost:      ______ EUR
  Tokens per second: ______

Power

  Power consumption: ______ W
  Cost of power:     ______ Cents per kWh

Usage

  Daily usage:        _____ h
  Years in use:       _____ years
  Work days per year: _____ days
```

## Implementation notes

The app is a single HTML file with all necessary CSS and JavaScript inlined.

The app is self-contained and has no external dependencies on CSS or JavaScript files. 
