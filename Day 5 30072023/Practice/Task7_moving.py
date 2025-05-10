home_length: int = int(input())
home_width: int = int(input())
home_height: int = int(input())

home_volume: int = home_height * home_width * home_length

completed = False

while not completed:
    count_boxes = input()

    if count_boxes == "Done":
        print(f"{home_volume} Cubic meters left.")
        completed = True
        break

    home_volume -= int(count_boxes)

    if home_volume <= 0:
        completed = True
        print(f"No more free space! You need {abs(home_volume)} Cubic meters more.")
