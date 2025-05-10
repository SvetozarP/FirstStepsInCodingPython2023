number_days: int = int(input())
number_hours: int = int(input())
total_cost_day: float = 0.00
total_cost: float = 0.00

for day in range(1, number_days + 1):
    if day % 2 == 0:
        for hour in range(1, number_hours + 1):
            if hour % 2 == 1:
                total_cost_day += 2.5
            else:
                total_cost_day += 1
    elif day % 2 == 1:
        for hour in range(1, number_hours + 1):
            if hour % 2 == 0:
                total_cost_day += 1.25
            else:
                total_cost_day += 1
    print(f"Day: {day} - {total_cost_day:.2f} leva")
    total_cost += total_cost_day
    total_cost_day = 0.00

print(f"Total: {total_cost:.2f} leva")
