number_turns: int = int(input())

count_09: int = 0
count_1019: int = 0
count_2029: int = 0
count_3039: int = 0
count_4050: int = 0
count_invalid: int = 0
total_grades: float = 0

for _ in range(1, number_turns + 1):

    current_point: int = int(input())

    if 0 <= current_point <= 9:
        count_09 += 1
        total_grades += current_point * 0.2
    elif 10 <= current_point <= 19:
        count_1019 += 1
        total_grades += current_point * 0.3
    elif 20 <= current_point <= 29:
        count_2029 += 1
        total_grades += current_point * 0.4
    elif 30 <= current_point <= 39:
        count_3039 += 1
        total_grades += 50
    elif 40 <= current_point <= 50:
        count_4050 += 1
        total_grades += 100
    else:
        count_invalid += 1
        total_grades *= 0.5

print(f"{total_grades:.2f}")
print(f"From 0 to 9: {count_09 / number_turns * 100:.2f}%")
print(f"From 10 to 19: {count_1019 / number_turns * 100:.2f}%")
print(f"From 20 to 29: {count_2029 / number_turns * 100:.2f}%")
print(f"From 30 to 39: {count_3039 / number_turns * 100:.2f}%")
print(f"From 40 to 50: {count_4050 / number_turns * 100:.2f}%")
print(f"Invalid numbers: {count_invalid / number_turns * 100:.2f}%")
