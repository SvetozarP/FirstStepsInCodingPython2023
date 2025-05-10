from sys import maxsize

number_pairs: int = int(input())
max_diff: int = -maxsize
prev_sum: int = 0
diff: int = 0
sum_numbers: int = 0

for x in range(number_pairs):

    number1: int = int(input())
    number2: int = int(input())

    sum_numbers = number1 + number2

    if x == 0:
        prev_sum = sum_numbers

    else:
        diff = abs(prev_sum - sum_numbers)

        if diff > max_diff:
            max_diff = diff

    prev_sum = sum_numbers

if diff == 0:
    print(f"Yes, value={sum_numbers}")
else:
    print(f"No, maxdiff={max_diff}")