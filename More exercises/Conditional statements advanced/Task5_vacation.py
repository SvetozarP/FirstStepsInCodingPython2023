budget: float = float(input())
season: str = input()
location_v: str = ""
place_stay: str = ""
price: float = 0.0

if budget <= 1000:

    place_stay = "Camp"

    if season == "Summer":

        location_v = "Alaska"
        price = budget * 0.65

    elif season == "Winter":

        location_v = "Morocco"
        price = budget * 0.45

elif 1000 < budget <= 3000:

    place_stay = "Hut"

    if season == "Summer":

        location_v = "Alaska"
        price = budget * 0.8

    elif season == "Winter":

        location_v = "Morocco"
        price = budget * 0.6

elif budget > 3000:

    place_stay = "Hotel"
    price = budget * 0.9

    if season == "Summer":
        location_v = "Alaska"
    elif season == "Winter":
        location_v = "Morocco"

print(f"{location_v} - {place_stay} - {price:.2f}")
