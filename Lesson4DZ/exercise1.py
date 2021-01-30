from sys import argv
script_name, output_hours,rate_per_hour, bonus = argv
output_hours = int(output_hours)
rate_per_hour = int(rate_per_hour)
bonus = int(bonus)

print(f'Заработная плата сотрудника: {(output_hours* rate_per_hour)+bonus} р.')
