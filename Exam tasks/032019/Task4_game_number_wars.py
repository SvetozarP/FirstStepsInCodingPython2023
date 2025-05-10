name_player1: str = input()
name_player2: str = input()
player1_score: int = 0
player2_score: int = 0

while True:

    card1 = input()

    if card1 == "End of game":

        print(f"{name_player1} has {player1_score} points")
        print(f"{name_player2} has {player2_score} points")
        break

    card2 = int(input())

    if int(card1) == card2:
        card1_additional = int(input())
        card2_additional = int(input())

        if card1_additional > card2_additional:

            print("Number wars!")
            print(f"{name_player1} is winner with {player1_score} points")
            break

        elif card2_additional > card1_additional:

            print("Number wars!")
            print(f"{name_player2} is winner with {player2_score} points")
            break

    elif int(card1) > card2:

        player1_score += int(card1) - card2

    elif card2 > int(card1):

        player2_score += card2 - int(card1)
