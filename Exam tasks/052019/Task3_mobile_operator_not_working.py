contract_term: str = input()
contract_type: str = input()
internet_added: str = input()
count_months: int = int(input())
total_price: float = 0
price: float = 0

if contract_type == "Small":

    if contract_term == "one":
        price = 9.98
    elif contract_term == "two":
        price = 8.58

elif contract_term == "Middle":

    if contract_term == "one":
        price = 18.99
    elif contract_term == "two":
        price = 17.09

elif contract_type == "Large":

    if contract_term == "one":
        price = 25.98
    elif contract_term == "two":
        price = 23.59

elif contract_type == "ExtraLarge":

    if contract_term == "one":
        price = 35.99
    elif contract_term == "two":
        price = 31.79

if internet_added == "yes" and price > 0:

    if price <= 10:
        price += 5.5
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85

if contract_term == "two":
    total_price = price * count_months * (1 - 0.0375)
elif contract_term == "one":
    total_price = price * count_months

print(f"{total_price:.2f} lv.")
