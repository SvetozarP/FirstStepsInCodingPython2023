from math import ceil
height_wall: int = int(input())
width_wall: int = int(input())
perc_to_paint: int = int(input())
already_painted: int = 0

total_to_paint = ceil(4 * height_wall * width_wall * (1 - perc_to_paint / 100))

is_tired: bool = False
is_painted: bool = False

while True:

    to_paint: str = input()

    if to_paint == "Tired!":
        is_tired = True
        break

    already_painted += int(to_paint)

    if already_painted >= total_to_paint:
        is_painted = True
        break

if is_tired:
    print(f"{total_to_paint - already_painted} quadratic m left.")

if is_painted:
    if already_painted == total_to_paint:
        print("All walls are painted! Great job, Pesho!")
    elif already_painted > total_to_paint:
        print(f"All walls are painted and you have {already_painted - total_to_paint} l paint left!")
