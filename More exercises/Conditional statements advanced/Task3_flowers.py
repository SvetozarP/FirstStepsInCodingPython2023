bought_hrizantemi: int = int(input())
bought_roses: int = int(input())
bought_tulips: int = int(input())
season: str = input()
feast: str = input()
price_hrizantemi: float = 0.0
price_roses: float = 0.0
price_tulip: float = 0.0
bouquet_price: float = 0.0
total_bought: int = bought_roses + bought_hrizantemi + bought_tulips

if season == "Spring" or season == "Summer":

    price_hrizantemi = 2
    price_roses = 4.10
    price_tulip = 2.5

elif season == "Autumn" or season == "Winter":

    price_hrizantemi = 3.75
    price_roses = 4.5
    price_tulip = 4.15

if feast == "Y":

    price_hrizantemi *= 1.15
    price_roses *= 1.15
    price_tulip *= 1.15

bouquet_price = price_hrizantemi * bought_hrizantemi + price_roses * bought_roses + price_tulip * bought_tulips

if bought_tulips > 7 and season == "Spring":

    bouquet_price *= 0.95

if bought_roses >= 10 and season == "Winter":

    bouquet_price *= 0.9

if total_bought > 20:

    bouquet_price *= 0.8

bouquet_price += 2

print(f"{bouquet_price:.2f}")
