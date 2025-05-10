name_team: str = input()
games_played: int = int(input())
game_win: int = 0
game_draw: int = 0
game_lost: int = 0

if games_played < 1:
    print(f"{name_team} hasn't played any games during this season.")

else:

    for _ in range(1, games_played + 1):
        result: str = input()

        if result == "W":
            game_win += 1
        elif result == "D":
            game_draw += 1
        elif result == "L":
            game_lost += 1

    print(f"{name_team} has won {game_win * 3 + game_draw * 1} points during this season.")
    print("Total stats:")
    print(f"## W: {game_win}")
    print(f"## D: {game_draw}")
    print(f"## L: {game_lost}")
    print(f"Win rate: {game_win / games_played * 100:.2f}%")
