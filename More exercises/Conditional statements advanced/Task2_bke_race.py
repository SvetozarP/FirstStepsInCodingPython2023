count_juniors: int = int(input())
count_seniors: int = int(input())
type_race: str = input()
price_juniors: float = 0.0
price_seniors: float = 0.0
total_cost: float = 0.0

if type_race == "trail":

    price_juniors = 5.5
    price_seniors = 7

elif type_race == "cross-country":

    price_juniors = 8
    price_seniors = 9.5
    total_contestants: int = count_seniors + count_juniors

    if total_contestants >= 50:

        price_juniors *= 0.75
        price_seniors *= 0.75

elif type_race == "downhill":

    price_juniors = 12.25
    price_seniors = 13.75

elif type_race == "road":

    price_juniors = 20
    price_seniors = 21.5

total_cost = count_juniors * price_juniors + count_seniors * price_seniors

expense = total_cost * 0.05

cost_after_expense = total_cost - expense

print(f"{cost_after_expense:.2f}")
