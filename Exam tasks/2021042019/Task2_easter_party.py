number_guests: int = int(input())
price_deposit_per_person: float = float(input())
desi_budget: float = float(input())

cake_price = desi_budget * 0.1

if 10 <= number_guests <= 15:
    price_deposit_per_person *= 0.85

elif 15 < number_guests <= 20:
    price_deposit_per_person *= 0.8

elif number_guests > 20:
    price_deposit_per_person *= 0.75

party_price = price_deposit_per_person * number_guests + cake_price

if party_price <= desi_budget:
    print(f"It is party time! {desi_budget - party_price:.2f} leva left.")
elif party_price > desi_budget:
    print(f"No party! {party_price - desi_budget:.2f} leva needed.")
