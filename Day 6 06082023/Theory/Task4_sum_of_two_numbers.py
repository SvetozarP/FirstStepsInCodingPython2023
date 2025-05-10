range_start: int = int(input())
range_end: int = int(input())
magic_number: int = int(input())
combination_count = 0
number1 = range_start
number2 = range_start
found = False

for number1 in range(range_start, range_end + 1):
    if not found:
        for number2 in range(range_start, range_end + 1):
            combination_count += 1
            if number1 + number2 == magic_number:
                print(f"Combination N:{combination_count} ({number1} + {number2} = {magic_number})")
                found = True
                break
            elif number1 == range_end and number2 == range_end:
                print(f"{combination_count} combinations - neither equals {magic_number}")
