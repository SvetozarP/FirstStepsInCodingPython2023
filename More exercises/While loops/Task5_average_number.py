n: int = int(input())
total: int = 0

for _ in range(1, n + 1):

    number: int = int(input())
    total += number

print(f"{total / n:.2f}")
