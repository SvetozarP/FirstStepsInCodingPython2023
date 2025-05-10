name_movie: str = input()
purch_pack: str = input()
number_tickets: int = int(input())
price_purch: int = 0
discount: float = 1.00
total_price: float = 0.00

if name_movie == "John Wick":

    if purch_pack == "Drink":
        price_purch = 12 * number_tickets

    elif purch_pack == "Popcorn":
        price_purch = 15 * number_tickets

    elif purch_pack == "Menu":
        price_purch = 19 * number_tickets

elif name_movie == "Star Wars":

    if purch_pack == "Drink":
        price_purch = 18 * number_tickets

    elif purch_pack == "Popcorn":
        price_purch = 25 * number_tickets

    elif purch_pack == "Menu":
        price_purch = 30 * number_tickets

    if number_tickets >= 4:
        discount = 0.7

elif name_movie == "Jumanji":

    if purch_pack == "Drink":
        price_purch = 9 * number_tickets

    elif purch_pack == "Popcorn":
        price_purch = 11 * number_tickets

    elif purch_pack == "Menu":
        price_purch = 14 * number_tickets

    if number_tickets == 2:
        discount = 0.85

total_price = price_purch * discount

print(f"Your bill is {total_price:.2f} leva.")
