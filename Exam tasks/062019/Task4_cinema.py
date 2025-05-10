room_capacity: int = int(input())
space_taken: int = 0
people_in: str = ""
total_price: int = 0
is_full: bool = False

while True:

    people_in = input()

    if people_in == "Movie time!":

        break

    space_taken += int(people_in)

    if space_taken > room_capacity:

        is_full = True
        break

    elif int(people_in) % 3 == 0:

        total_price += int(people_in) * 5 - 5

    else:

        total_price += int(people_in) * 5

if is_full:
    print("The cinema is full.")
else:
    print(f"There are {room_capacity - space_taken} seats left in the cinema.")

print(f"Cinema income - {total_price} lv.")
