season: str = input()
km_month: float = float(input())
price_km: float = 0.0
pay_season: float = 0.0

if km_month < 5000:

    if season == "Spring" or season == "Autumn":

        price_km = 0.75

    elif season == "Summer":

        price_km = 0.9

    elif season == "Winter":

        price_km = 1.05

elif 5000 < km_month <= 10000:

    if season == "Spring" or season == "Autumn":

        price_km = 0.95

    elif season == "Summer":

        price_km = 1.1

    elif season == "Winter":

        price_km = 1.25

elif 10000 < km_month <= 20000:

        price_km = 1.45

pay_season = km_month * price_km * 0.9 * 4

print(f"{pay_season:.2f}")
