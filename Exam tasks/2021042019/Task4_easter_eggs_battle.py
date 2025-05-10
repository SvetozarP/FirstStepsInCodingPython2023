player1_eggs: int = int(input())
player2_eggs: int = int(input())

while player1_eggs != 0 and player2_eggs != 0:
    winner: str = input()

    if winner == "End":

        print(f"Player one has {player1_eggs} eggs left.")
        print(f"Player two has {player2_eggs} eggs left.")

        break

    elif winner == "one":

        player2_eggs -= 1

    elif winner == "two":

        player1_eggs -= 1

else:

    if player2_eggs > 0:

        print(f"Player one is out of eggs. Player two has {player2_eggs} eggs left.")

    elif player1_eggs > 0:

        print(f"Player two is out of eggs. Player one has {player1_eggs} eggs left.")