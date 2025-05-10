budget = int(input())
season = input()
c_fishermen = int(input())
rent = 0

if season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Spring":
    rent = 3000
elif season == "Winter":
    rent = 2600

if c_fishermen <= 6:
    trip_price = rent - rent * 0.1
elif 6 < c_fishermen <= 11:
    trip_price = rent - rent * 0.15
else:
    trip_price = rent - rent * 0.25

if season != "Autumn" and c_fishermen % 2 == 0:
    trip_price = trip_price - (trip_price * 0.05)

if budget >= trip_price:
    print(f'Yes! You have {budget - trip_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {trip_price - budget:.2f} leva.')
