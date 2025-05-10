budget = int(input())
season = input()
count_fishermen = int(input())
ship_rent = 0
discount = 0
add_discount = 0


if season == "Spring":

    ship_rent = 3000

    if count_fishermen % 2 == 0:
        add_discount = 0.05

    if 0 < count_fishermen <= 6:
        discount = 0.1
    elif 6 < count_fishermen <= 11:
        discount = 0.15
    elif count_fishermen >= 12:
        discount = 0.25
    else:
        exit(1)

    price = ship_rent - ship_rent * discount - ship_rent * add_discount

elif season == "Summer":
    ship_rent = 4200

    if count_fishermen % 2 == 0:
        add_discount = 0.05

    if 0 < count_fishermen <= 6:
        discount = 0.1
    elif 6 < count_fishermen <= 11:
        discount = 0.15
    elif count_fishermen >= 12:
        discount = 0.25
    else:
        exit(1)

    price = ship_rent - ship_rent * discount - ship_rent * add_discount

elif season == "Autumn":
    ship_rent = 4200

    if 0 < count_fishermen <= 6:
        discount = 0.1
    elif 6 < count_fishermen <= 11:
        discount = 0.15
    elif count_fishermen >= 12:
        discount = 0.25
    else:
        exit(1)

    price = ship_rent - ship_rent * discount

elif season == "Winter":
    ship_rent = 2600

    if count_fishermen % 2 == 0:
        add_discount = 0.05

    if 0 < count_fishermen <= 6:
        discount = 0.1
    elif 6 < count_fishermen <= 11:
        discount = 0.15
    elif count_fishermen >= 12:
        discount = 0.25
    else:
        exit(1)

    price = ship_rent - ship_rent * discount - ship_rent * add_discount

else:
    exit(1)

if budget >= price:
    mon_left = budget - price
    print(f"Yes! You have {mon_left:.2f} leva left.")

else:
    mon_left = price - budget
    print(f"Not enough money! You need {mon_left:.2f} leva.")
