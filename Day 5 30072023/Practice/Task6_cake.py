cake_length = int(input())
cake_width = int(input())

total_cake_pieces: int = cake_length * cake_width

cake_finish = False

while not cake_finish:
    count_pieces = input()

    if count_pieces == "STOP":
        cake_finish = True
        print(f"{total_cake_pieces} pieces are left.")
        break

    total_cake_pieces -= int(count_pieces)
    if total_cake_pieces <= 0:
        cake_finish = True
        print(f"No more cake left! You need {abs(total_cake_pieces)} pieces more.")
