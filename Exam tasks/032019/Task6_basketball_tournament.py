count_win: int = 0
count_lost: int = 0

while True:

    name_tournament: str = input()

    if name_tournament == "End of tournaments":
        total_games: int = count_lost + count_win
        print(f"{count_win / total_games * 100:.2f}% matches win")
        print(f"{count_lost / total_games * 100:.2f}% matches lost")
        break

    number_games: int = int(input())

    for game in range(1, number_games + 1):

        desi_points: int = int(input())
        opponent_points: int = int(input())

        if desi_points > opponent_points:

            print(f"Game {game} of tournament {name_tournament}: win with {desi_points - opponent_points} points.")
            count_win += 1

        elif desi_points < opponent_points:

            print(f"Game {game} of tournament {name_tournament}: lost with {opponent_points - desi_points} points.")
            count_lost += 1
