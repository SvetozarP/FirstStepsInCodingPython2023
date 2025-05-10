n: int = int(input())

for col in range(1, n + 1):
    for _ in range(0, col):
        print("$", end=" ")
    print("")
