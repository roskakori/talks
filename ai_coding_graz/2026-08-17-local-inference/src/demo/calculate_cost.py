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