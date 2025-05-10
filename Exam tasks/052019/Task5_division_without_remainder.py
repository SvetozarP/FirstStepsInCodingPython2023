count_numbers: int = int(input())

divide_by_two: int = 0
divide_by_three: int = 0
divide_by_four: int = 0
number_in: int = 0

while number_in < count_numbers:
    number: int = int(input())

    if number % 2 == 0:
        divide_by_two += 1

    if number % 3 == 0:
        divide_by_three += 1

    if number % 4 == 0:
        divide_by_four += 1

    number_in += 1

print(f"{divide_by_two / count_numbers * 100:.2f}%")
print(f"{divide_by_three / count_numbers * 100:.2f}%")
print(f"{divide_by_four / count_numbers * 100:.2f}%")
