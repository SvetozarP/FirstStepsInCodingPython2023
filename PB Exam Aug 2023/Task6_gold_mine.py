number_locations: int = int(input())
gold_per_loc: float = 0.0
avg_per_day: float = 0.0

for _ in range(number_locations):

    gold_harvest: float = float(input())
    days_at_location: int = int(input())

    for _ in range(days_at_location):

        gold_mined: float = float(input())
        gold_per_loc += gold_mined

    avg_per_day = gold_per_loc / days_at_location
    gold_per_loc = 0

    if avg_per_day >= gold_harvest:
        print(f"Good job! Average gold per day: {avg_per_day:.2f}.")
    elif avg_per_day < gold_harvest:
        print(f"You need {abs(avg_per_day - gold_harvest):.2f} gold.")
