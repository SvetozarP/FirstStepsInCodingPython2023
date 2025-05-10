count_floors: int = int(input())
count_rooms: int = int(input())
current_floor: int = count_floors
current_room: int = 0

for current_floor in range(count_floors, 0, -1):
    for current_room in range(0, count_rooms):
        if current_floor == count_floors:
            print("L{0}{1} ".format(current_floor, current_room), end="")

# The str.format() method of strings requires more manual effort. You’ll still use { and }
# to mark where a variable will be substituted and can provide detailed formatting directives,
# but you’ll also need to provide the information to be formatted.

        elif current_floor % 2 == 0:
            print("O{0}{1} ".format(current_floor, current_room), end="")
        else:
            print("A{0}{1} ".format(current_floor, current_room), end="")
    print("")
