n: int = int(input())

for i in range((n + 1) // 2):
    if i == 0:
        if not n % 2:
            print(f"{'-' * ((n - 2) // 2)}**{'-' * ((n - 2) // 2)}")
        else:
            print(f"{'-' * ((n - 1) // 2)}*{'-' * ((n - 1) // 2)}")
    else:
        if not n % 2:
            print(f"{'-' * ((n - (i + 1) * 2) // 2)}{'*' * ((i + 1) * 2)}{'-' * ((n - (i + 1) * 2) // 2)}")
        else:
            print(f"{'-' * ((n + 1 - (i + 1) * 2) // 2)}{'*' * ((i+ 1) * 2 - 1)}{'-' * ((n + 1 - ( i + 1) * 2) // 2)}")

for i in range(n - (n + 1) // 2):
    print(f"|{'*' * (n - 2)}|")
