month = input()
sleeps = int(input())
price_studio = 0
price_apart = 0

if month == "May" or month == "October":
    if sleeps <= 7:
        price_studio = sleeps * 50
        price_apart = sleeps * 65
        print(f"Apartment: {price_apart:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")
    elif 7 < sleeps <= 14:
        price_studio = sleeps * 50
        price_studio *= 0.95
        price_apart = sleeps * 65
        print(f"Apartment: {price_apart:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")
    elif sleeps > 14:
        price_studio = sleeps * 50
        price_studio *= 0.7
        price_apart = sleeps * 65
        price_apart *= 0.9
        print(f"Apartment: {price_apart:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")

elif month == "June" or month == "September":
    if sleeps <= 7:
        price_studio = sleeps * 75.2
        price_apart = sleeps * 68.7
        print(f"Apartment: {price_apart:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")
    elif 7 < sleeps <= 14:
        price_studio = sleeps * 75.2
        price_apart = sleeps * 68.7
        print(f"Apartment: {price_apart:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")
    elif sleeps > 14:
        price_studio = sleeps * 75.2
        price_studio *= 0.8
        price_apart = sleeps * 68.7
        price_apart *= 0.9
        print(f"Apartment: {price_apart:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")

elif month == "July" or month == "August":
    if sleeps <= 7:
        price_studio = sleeps * 76
        price_apart = sleeps * 77
        print(f"Apartment: {price_apart:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")
    elif 7 < sleeps <= 14:
        price_studio = sleeps * 76
        price_apart = sleeps * 77
        print(f"Apartment: {price_apart:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")
    elif sleeps > 14:
        price_studio = sleeps * 76
        price_apart = sleeps * 77
        price_apart *= 0.9
        print(f"Apartment: {price_apart:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")
