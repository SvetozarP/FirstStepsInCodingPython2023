movie_budget = float(input())
num_statists = int(input())
price_cloth_one = float(input())

price_decor = movie_budget * 0.1

if num_statists > 150:
    price_cloth_one = price_cloth_one - (price_cloth_one * 0.1)

total_expense = num_statists * price_cloth_one + price_decor

if total_expense > movie_budget:
    mon_needed = total_expense - movie_budget
    print("Not enough money!")
    print(f"Wingard needs {mon_needed:.2f} leva more.")

else:
    mon_extra = movie_budget - total_expense
    print("Action!")
    print(f"Wingard starts filming with {mon_extra:.2f} leva left.")
