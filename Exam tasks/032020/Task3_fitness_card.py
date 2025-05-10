budget: float = float(input())
sex: str = input()
age: int = int(input())
sport: str = input()

price: float = 0

if sex == "m":
    if sport == "Gym":

        price = 42

        if age <= 19:
            price *= 0.8

    elif sport == "Boxing":

        price = 41

        if age <= 19:
            price *= 0.8

    elif sport == "Yoga":

        price = 45

        if age <= 19:
            price *= 0.8

    elif sport == "Zumba":

        price = 34

        if age <= 19:
            price *= 0.8

    elif sport == "Dances":

        price = 51

        if age <= 19:
            price *= 0.8

    elif sport == "Pilates":

        price = 39

        if age <= 19:
            price *= 0.8

elif sex == "f":
    if sport == "Gym":

        price = 35

        if age <= 19:
            price *= 0.8

    elif sport == "Boxing":

        price = 37

        if age <= 19:
            price *= 0.8

    elif sport == "Yoga":

        price = 42

        if age <= 19:
            price *= 0.8

    elif sport == "Zumba":

        price = 31

        if age <= 19:
            price *= 0.8

    elif sport == "Dances":

        price = 53

        if age <= 19:
            price *= 0.8

    elif sport == "Pilates":

        price = 37

        if age <= 19:
            price *= 0.8

if budget >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${abs(budget - price):.2f} more.")
