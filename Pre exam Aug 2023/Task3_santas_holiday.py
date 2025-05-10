days_stay: int = int(input())
type_room: str = input()
feedback: str = input()

nights_stay = days_stay - 1

price: int = 0
total_price: float = 0

if type_room == "room for one person":
    price = 18
elif type_room == "apartment":
    price = 25

    if days_stay < 10:
        price *= 0.7
    elif 10 <= days_stay <= 15:
        price *= 0.65
    elif days_stay > 15:
        price *= 0.5

elif type_room == "president apartment":
    price = 35

    if days_stay < 10:
        price *= 0.9
    elif 10 <= days_stay <= 15:
        price *= 0.85
    elif days_stay > 15:
        price *= 0.8

total_price = nights_stay * price

if feedback == "positive":
    total_price *= 1.25
if feedback == "negative":
    total_price *= 0.9

print(f"{total_price:.2f}")
