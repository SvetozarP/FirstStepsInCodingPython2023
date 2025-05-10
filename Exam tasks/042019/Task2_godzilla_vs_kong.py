budget = float(input())
n_statists = int(input())
price_per_one_statist = float(input())
decor_price = budget * 0.1

if n_statists > 150:
    price_per_one_statist *= 0.9

total_price = n_statists * price_per_one_statist + decor_price

if budget >= total_price:
    money_left = budget - total_price
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")

elif budget < total_price:
    money_need = total_price - budget
    print("Not enough money!")
    print(f"Wingard needs {money_need:.2f} leva more.")
