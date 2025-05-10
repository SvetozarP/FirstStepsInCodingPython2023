from sys import maxsize

is_stopped: bool = False
player_score: int = 0
count: int = 0
max_score = -maxsize
current_name: str = ""

while True:
    name_player: str = input()
    count += 1

    if name_player == "Stop":
        is_stopped = True
        break

    else:
        player_score = 0
        for index, digit in enumerate(name_player):

            score_digit = ord(digit)
            score: int = int(input())

            if score_digit == score:
                player_score += 10
            else:
                player_score += 2

        if player_score >= max_score:
            current_name = name_player
            max_score = player_score

print(f"The winner is {current_name} with {max_score} points!")
