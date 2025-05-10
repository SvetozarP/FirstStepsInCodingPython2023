drink: str = input()
option: str = input()
number_drinks: int = int(input())
price: float = 0.00
discount_without: float = 1.00
discount_number: float = 1.00
discount_price: float = 1.00
total_price: float = 0

if drink == "Espresso":

    if option == "Without":
        price = 0.9
        discount_without = 0.65
    elif option == "Normal":
        price = 1
    elif option == "Extra":
        price = 1.2

elif drink == "Cappuccino":

    if option == "Without":
        price = 1
        discount_without = 0.65
    elif option == "Normal":
        price = 1.2
    elif option == "Extra":
        price = 1.6

elif drink == "Tea":

    if option == "Without":
        price = 0.5
        discount_without = 0.65
    elif option == "Normal":
        price = 0.6
    elif option == "Extra":
        price = 0.7

total_price = price * number_drinks * discount_without

if number_drinks >= 5 and drink == "Espresso":
    discount_number = 0.75

total_price = total_price * discount_number

if total_price > 15:
    discount_price = 0.8

total_price = total_price * discount_price

print(f"You bought {number_drinks} cups of {drink} for {total_price:.2f} lv.")
