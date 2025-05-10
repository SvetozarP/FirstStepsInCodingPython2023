player_name: str = input()
total_points: int = 301
successful_hits: int = 0
unsuccessful_hits: int = 0

while True:

    shot_zone = input()

    if shot_zone == "Retire":
        print(f"{player_name} retired after {unsuccessful_hits} unsuccessful shots.")
        break

    points = int(input())

    if shot_zone == "Double":
        points *= 2
    elif shot_zone == "Triple":
        points *= 3

    if points < total_points:

        successful_hits += 1
        total_points -= points

    elif points > total_points:

        unsuccessful_hits += 1

    elif points == total_points:
        successful_hits += 1
        total_points -= points
        print(f"{player_name} won the leg with {successful_hits} shots.")
        break
