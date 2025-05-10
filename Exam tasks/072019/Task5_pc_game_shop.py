games_sold: int = int(input())
hearthstone_sold: int = 0
fortnite_sold: int = 0
overwatch_sold: int = 0
others_sold: int = 0

for _ in range(1, games_sold + 1):
    game_name: str = input()

    if game_name == "Hearthstone":
        hearthstone_sold += 1
    elif game_name == "Fornite":
        fortnite_sold += 1
    elif game_name == "Overwatch":
        overwatch_sold += 1
    else:
        others_sold += 1

print(f"Hearthstone - {(hearthstone_sold / games_sold * 100):.2f}%")
print(f"Fornite - {(fortnite_sold / games_sold * 100):.2f}%")
print(f"Overwatch - {(overwatch_sold / games_sold * 100):.2f}%")
print(f"Others - {(others_sold / games_sold* 100):.2f}%")
