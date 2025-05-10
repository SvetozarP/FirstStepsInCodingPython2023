budget: float = float(input())
fuel_need: float = float(input())
day_week: str = input()

price_fuel = fuel_need * 2.1
price_excursion = 100 + price_fuel

if day_week == "Saturday":
    price_excursion = price_excursion * 0.9
elif day_week == "Sunday":
    price_excursion = price_excursion * 0.8

diff = abs(budget - price_excursion)

if budget >= price_excursion:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
