size_egg: str = input()
colour_egg: str = input()
number_eggs: int = int(input())
price: int = 0
manuf_expense: float = 0
total_price: float = 0

if size_egg == "Large":

    if colour_egg == "Red":
        price = 16
    elif colour_egg == "Green":
        price = 12
    elif colour_egg == "Yellow":
        price = 9

elif size_egg == "Medium":

    if colour_egg == "Red":
        price = 13
    elif colour_egg == "Green":
        price = 9
    elif colour_egg == "Yellow":
        price = 7

elif size_egg == "Small":

    if colour_egg == "Red":
        price = 9
    elif colour_egg == "Green":
        price = 8
    elif colour_egg == "Yellow":
        price = 5

manuf_expense = price * number_eggs * 0.35
total_price = price * number_eggs - manuf_expense

print(f"{total_price:.2f} leva.")
