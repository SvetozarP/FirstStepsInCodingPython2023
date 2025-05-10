from math import ceil

number_guests: int = int(input())
lubo_budget: int = int(input())

price_kozunak: int = 4
price_egg: float = 0.45

number_kozunak = ceil(number_guests / 3)
number_egg = number_guests * 2

total_cost = number_kozunak * price_kozunak + number_egg * price_egg

if total_cost <= lubo_budget:
    print(f"Lyubo bought {number_kozunak} Easter bread and {number_egg} eggs.")
    print(f"He has {lubo_budget - total_cost:.2f} lv. left.")
elif total_cost > lubo_budget:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {total_cost - lubo_budget:.2f} lv. more.")
