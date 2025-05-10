from math import floor
n_tournaments = int(input())
start_points = int(input())
init_points = start_points
count_wins = 0

for i in range(1, n_tournaments+1):
    positioning = input()
    if positioning == "W":
        count_wins += 1
        init_points += 2000
    elif positioning == "F":
        init_points += 1200
    elif positioning == "SF":
        init_points += 720

average_points = floor((init_points - start_points) / n_tournaments)
percentage_win = count_wins / n_tournaments * 100

print(f"Final points: {init_points}")
print(f"Average points: {average_points}")
print(f"{percentage_win:.2f}%")
