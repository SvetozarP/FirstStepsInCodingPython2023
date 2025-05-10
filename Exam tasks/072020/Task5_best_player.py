from sys import maxsize
max_goals: int = -maxsize
best_player: str = ""

while True:

    player_name: str = input()

    if player_name == "END":
        print(f"{best_player} is the best player!")
        if max_goals // 3 > 0:
            print(f"He has scored {max_goals} goals and made a hat-trick !!!")
        elif max_goals // 3 == 0:
            print(f"He has scored {max_goals} goals.")
        break

    number_goals: int = int(input())

    if max_goals < number_goals:
        max_goals = number_goals
        best_player = player_name

    if number_goals >= 10:
        print(f"{best_player} is the best player!")
        if max_goals // 3 > 0:
            print(f"He has scored {max_goals} goals and made a hat-trick !!!")
        elif max_goals // 3 == 0:
            print(f"He has scored {max_goals} goals.")
        break
