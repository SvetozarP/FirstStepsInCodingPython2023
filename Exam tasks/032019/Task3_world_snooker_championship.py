comp_stage: str = input()
type_ticket: str = input()
number_tickets: int = int(input())
trophy_photo: str = input()
price_per_ticket: float = 0.00
price_for_tickets: float = 0.00

if trophy_photo == "Y":

    price_photo: int = 40
else:
    price_photo: int = 0

if comp_stage == "Quarter final":

    if type_ticket == "Standard":
        price_per_ticket = 55.5
    elif type_ticket == "Premium":
        price_per_ticket = 105.2
    elif type_ticket == "VIP":
        price_per_ticket = 118.9

elif comp_stage == "Semi final":

    if type_ticket == "Standard":
        price_per_ticket = 75.88
    elif type_ticket == "Premium":
        price_per_ticket = 125.22
    elif type_ticket == "VIP":
        price_per_ticket = 300.4

elif comp_stage == "Final":

    if type_ticket == "Standard":
        price_per_ticket = 110.1
    elif type_ticket == "Premium":
        price_per_ticket = 160.66
    elif type_ticket == "VIP":
        price_per_ticket = 400

price_for_tickets = price_per_ticket * number_tickets

if price_for_tickets > 4000:
    price_for_tickets = price_for_tickets * 0.75
elif price_for_tickets > 2000:
    price_for_tickets = price_for_tickets * 0.9 + price_photo * number_tickets
else:
    price_for_tickets = price_for_tickets + price_photo * number_tickets

print(f"{price_for_tickets:.2f}")
