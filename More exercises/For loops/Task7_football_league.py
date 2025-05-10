capacity: int = int(input())
total_fans: int = int(input())
count_a: int = 0
count_b: int = 0
count_v: int = 0
count_g: int = 0

for _ in range(total_fans):

    sector: str = input()

    if sector == "A":
        count_a += 1
    elif sector == "B":
        count_b += 1
    elif sector == "V":
        count_v += 1
    elif sector == "G":
        count_g += 1

print(f"{count_a / total_fans * 100:.2f}%")
print(f"{count_b / total_fans * 100:.2f}%")
print(f"{count_v / total_fans * 100:.2f}%")
print(f"{count_g / total_fans * 100:.2f}%")
print(f"{total_fans / capacity * 100:.2f}%")
