n: int = int(input())

for row in range(1, n + 1):
    for col in range(1, n + 1 - row):
        print(" ", end="")
    print("*", end="")
    for col in range(1, row):
        print(" *", end="")
    print("")

for row in reversed(range(1, n)):
    for col in range(1, n + 1 - row):
        print(" ", end="")
    print("*", end="")
    for col in range(1, row):
        print(" *", end="")
    print("")
