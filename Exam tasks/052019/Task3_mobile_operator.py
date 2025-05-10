contract_term: str = input()
contract_type: str = input()
internet_added: str = input()
count_months: int = int(input())
total_price: float = 0
price: float = 0
discount: float = 1.00

if contract_term == "one":

    if contract_type == "Small":
        price = 9.98
    elif contract_type == "Middle":
        price = 18.99
    elif contract_type == "Large":
        price = 25.98
    elif contract_type == "ExtraLarge":
        price = 35.99

elif contract_term == "two":
    discount = 0.9625
    if contract_type == "Small":
        price = 8.58
    elif contract_type == "Middle":
        price = 17.09
    elif contract_type == "Large":
        price = 23.59
    elif contract_type == "ExtraLarge":
        price = 31.79

if internet_added == "yes" and price > 0:

    if price <= 10:
        price += 5.5
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85

total_price = price * count_months * discount

print(f"{total_price:.2f} lv.")
