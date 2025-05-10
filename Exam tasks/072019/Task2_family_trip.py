budget = float(input())
n_nights = int(input())
price_per_night = float(input())
perc_extra_expense = int(input())

if n_nights > 7:
    price_per_night *= 0.95

total_price = n_nights * price_per_night + budget * perc_extra_expense / 100

if budget >= total_price:
    money_left = budget - total_price
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
elif total_price > budget:
    money_need = total_price - budget
    print(f"{money_need:.2f} leva needed.")