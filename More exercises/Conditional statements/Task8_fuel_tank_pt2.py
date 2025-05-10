type_fuel: str = input()
qty_fuel: float = float(input())
card_own: str = input()

total_price: float = 0.0
price_per_ltr: float = 0.0

if type_fuel == "Gasoline":

    price_per_ltr = 2.22

    if card_own == "Yes":
        price_per_ltr -= 0.18

elif type_fuel == "Diesel":

    price_per_ltr = 2.33

    if card_own == "Yes":
        price_per_ltr -= 0.12

elif type_fuel == "Gas":

    price_per_ltr = 0.93

    if card_own == "Yes":
        price_per_ltr -= 0.08

total_price = qty_fuel * price_per_ltr

if 20 <= qty_fuel <= 25:

    total_price *= 0.92

elif qty_fuel > 25:

    total_price *= 0.9

print(f"{total_price:.2f} lv.")
