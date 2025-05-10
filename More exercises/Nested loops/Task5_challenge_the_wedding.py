number_men: int = int(input())
number_women: int = int(input())
max_tables: int = int(input())

while True:

    for man in range(1, number_men + 1):
        for woman in range(1, number_women + 1):

            if max_tables == 0:
                break
            print(f"({man} <-> {woman})", end=" ")
            max_tables -= 1

    break
