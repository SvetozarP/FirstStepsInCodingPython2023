days_stay: int = int(input())
hours_stay: int = int(input())
total_pay: float = 0.0
pay_for_day: float = 0.0

for day in range(1, days_stay + 1):

    for hour in range(1, hours_stay + 1):

        if not day % 2 and hour % 2:
            pay_for_day += 2.5
        elif day % 2 and not hour % 2:
            pay_for_day += 1.25
        else:
            pay_for_day += 1

    print(f"Day: {day} - {pay_for_day:.2f} leva")
    total_pay += pay_for_day
    pay_for_day = 0

print(f"Total: {total_pay:.2f} leva")
