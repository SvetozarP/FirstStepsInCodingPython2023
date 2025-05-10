rooms_per_floor = 6
floors = 4
for floor in reversed(range(1, floors + 1)):

    room_type = "A" if floor % 2 else "O"

    for room in range(rooms_per_floor):

        room_name = f"{room_type}{floor}{room}"
        print(room_name, end=" ")

    print()
