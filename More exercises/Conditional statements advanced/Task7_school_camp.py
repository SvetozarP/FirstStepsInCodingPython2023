season: str = input()
group_type: str = input()
number_students: int = int(input())
number_nights: int = int(input())
price: float = 0.0
type_sport: str = ""
total_price: float = 0.0

if season == "Winter":

    if group_type == "boys":

        price = 9.6
        type_sport = "Judo"

    elif group_type == "girls":

        price = 9.6
        type_sport = "Gymnastics"

    elif group_type == "mixed":

        price = 10
        type_sport = "Ski"

elif season == "Spring":

    if group_type == "boys":

        price = 7.2
        type_sport = "Tennis"

    elif group_type == "girls":

        price = 7.2
        type_sport = "Athletics"

    elif group_type == "mixed":

        price = 9.5
        type_sport = "Cycling"

elif season == "Summer":

    if group_type == "boys":

        price = 15
        type_sport = "Football"

    elif group_type == "girls":

        price = 15
        type_sport = "Volleyball"

    elif group_type == "mixed":

        price = 20
        type_sport = "Swimming"

total_price = number_students * number_nights * price

if 10 <= number_students < 20:

    total_price *= 0.95

elif 20 <= number_students < 50:

    total_price *= 0.85

elif number_students >= 50:

    total_price *= 0.5

print(f"{type_sport} {total_price:.2f} lv.")
