type_pastry: str = input()
number_ordered: int = int(input())
day_of_dec: int = int(input())
price: float = 0.0
total_price: float = 0.0

if day_of_dec <= 15:

    if type_pastry == "Cake":
        price = 24
    elif type_pastry == "Souffle":
        price = 6.66
    elif type_pastry == "Baklava":
        price = 12.6

elif day_of_dec > 15:

    if type_pastry == "Cake":
        price = 28.7
    elif type_pastry == "Souffle":
        price = 9.8
    elif type_pastry == "Baklava":
        price = 16.98

total_price = number_ordered * price

if day_of_dec <= 22:
    if 100 <= total_price <= 200:
        total_price *= 0.85
    elif total_price > 200:
        total_price *= 0.75

if day_of_dec <= 15:
    total_price *= 0.9

print(f"{total_price:.2f}")
