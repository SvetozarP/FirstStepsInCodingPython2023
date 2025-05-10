budget = float(input())
season = input()
pc_budget = 0
destination = 0
type_rest = 0

if season == "summer":
    type_rest = "Camp"

elif season == "winter":
    type_rest = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget *= 0.3
    elif season == "winter":
        budget *= 0.7

elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget *= 0.4
    if season == "winter":
        budget *= 0.8

elif budget > 1000:
    destination = "Europe"
    budget *= 0.9
    type_rest = "Hotel"



print(f"Somewhere in {destination}")
print(f"{type_rest} - {budget:.2f}")
