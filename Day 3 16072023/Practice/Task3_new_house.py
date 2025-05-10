typ_flower = input()
num_flower = int(input())
budget = int(input())
discount = 0
price = 0

if typ_flower == "Roses":
    price = 5.00
    if num_flower > 80:
        discount = 0.1

elif typ_flower == "Dahlias":
    price = 3.8
    if num_flower > 90:
        discount = 0.15

elif typ_flower == "Tulips":
    price = 2.8
    if num_flower > 80:
        discount = 0.15

elif typ_flower == "Narcissus":
    price = 3
    if num_flower < 120:
        discount = -0.15

elif typ_flower == "Gladiolus":
    price = 2.5
    if num_flower < 80:
        discount = -0.2

total_price_no_disc = num_flower * price
total_price = total_price_no_disc - (total_price_no_disc * discount)

if budget >= total_price:
    mon_left = budget - total_price
    print(f"Hey, you have a great garden with {num_flower} {typ_flower} and {mon_left:.2f} leva left.")

elif budget < total_price:
    mon_left = total_price - budget
    print(f"Not enough money, you need {mon_left:.2f} leva more.")
