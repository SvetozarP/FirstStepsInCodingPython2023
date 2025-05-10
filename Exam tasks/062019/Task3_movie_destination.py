movie_budget: float = float(input())
destination: str = input()
season: str = input()
days_filming: int = int(input())

filming_price: float = 0.00
diff: float = 0

if destination == "Dubai":

    if season == "Winter":
        filming_price = 45000 * days_filming * 0.7

    elif season == "Summer":
        filming_price = 40000 * days_filming * 0.7

elif destination == "Sofia":

    if season == "Winter":
        filming_price = 17000 * days_filming * 1.25

    elif season == "Summer":
        filming_price = 12500 * days_filming * 1.25

elif destination == "London":

    if season == "Winter":
        filming_price = 24000 * days_filming

    elif season == "Summer":
        filming_price = 20250 * days_filming


diff = abs(movie_budget - filming_price)

if movie_budget >= filming_price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")

else:
    print(f"The director needs {diff:.2f} leva more!")
