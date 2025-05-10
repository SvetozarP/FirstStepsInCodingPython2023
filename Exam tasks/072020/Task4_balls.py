from math import floor

count_balls: int = int(input())
total_points: int = 0
count_red_ball: int = 0
count_orange_ball: int = 0
count_yellow_ball: int = 0
count_white_ball: int = 0
count_black_ball: int = 0
count_other_ball: int = 0

for _ in range(1, count_balls + 1):

    colour_ball: str = input()

    if colour_ball == "red":
        total_points += 5
        count_red_ball += 1
    elif colour_ball == "orange":
        total_points += 10
        count_orange_ball += 1
    elif colour_ball == "yellow":
        total_points += 15
        count_yellow_ball += 1
    elif colour_ball == "white":
        total_points += 20
        count_white_ball += 1
    elif colour_ball == "black":
        total_points = floor(total_points / 2)
        count_black_ball += 1
    else:
        count_other_ball += 1
        continue

print(f"Total points: {total_points}")
print(f"Red balls: {count_red_ball}")
print(f"Orange balls: {count_orange_ball}")
print(f"Yellow balls: {count_yellow_ball}")
print(f"White balls: {count_white_ball}")
print(f"Other colors picked: {count_other_ball}")
print(f"Divides from black balls: {count_black_ball}")
