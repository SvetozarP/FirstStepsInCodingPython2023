destination: str = input()
dates_reservation: str = input()
number_nights: int = int(input())
price: int = 0

if destination == "France":

    if dates_reservation == "21-23":
        price = 30
    elif dates_reservation == "24-27":
        price = 35
    elif dates_reservation == "28-31":
        price = 40

elif destination == "Italy":

    if dates_reservation == "21-23":
        price = 28
    elif dates_reservation == "24-27":
        price = 32
    elif dates_reservation == "28-31":
        price = 39

elif destination == "Germany":

    if dates_reservation == "21-23":
        price = 32
    elif dates_reservation == "24-27":
        price = 37
    elif dates_reservation == "28-31":
        price = 43

print(f"Easter trip to {destination} : {number_nights * price:.2f} leva.")
