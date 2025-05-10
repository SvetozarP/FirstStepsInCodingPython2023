days_stay = int(input())
type_room = input()
feedback = input()
nights_stay = days_stay - 1
price = 0

if type_room == "room for one person":
    price = nights_stay * 18

elif type_room == "apartment":
    price = nights_stay * 25

    if nights_stay < 10:
        price *= 0.7
    elif 10 <= nights_stay <= 15:
        price *= 0.65
    elif nights_stay > 15:
        price *= 0.5

elif type_room == "president apartment":
    price = nights_stay * 35

    if nights_stay < 10:
        price *= 0.9
    elif 10 <= nights_stay <= 15:
        price *= 0.85
    elif nights_stay > 15:
        price *= 0.8

if feedback == "positive":
    price *= 1.25
elif feedback == "negative":
    price *= 0.9

print(f"{price:.2f}")
