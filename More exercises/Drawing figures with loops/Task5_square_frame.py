n: int = int(input())

for i in range (1, n + 1):
    for j in range(1, n + 1):

        if (i == 1 and j == 1) or (i == 1 and j == n) or (i == n and j == 1) or (i == n and j == n):
            to_print: str = "+"
        elif j == 1 or j == n:
            to_print: str = "|"
        else:
            to_print = "-"

        print(f"{to_print}", end=" ")
    print("")
