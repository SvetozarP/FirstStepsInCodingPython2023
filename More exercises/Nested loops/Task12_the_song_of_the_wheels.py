M: int = int(input())
count_pass: int = 0
found_number: str = ""

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):

                if a < b and c > d and a * b + c * d == M:
                    print(f"{a}{b}{c}{d}", end=" ")
                    count_pass += 1

                    if count_pass == 4:
                        found_number = str(a) + str(b) + str(c) + str(d)

if found_number != "":
    print("")
    print(f"Password: {found_number}")
else:
    print()
    print("No!")
