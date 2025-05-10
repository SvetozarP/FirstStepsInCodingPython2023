number: str = input()

first_number = int(number[0])
second_number = int(number[1])
third_number = int(number[2])

for number_1 in range(1, third_number + 1):
    for number_2 in range(1, second_number + 1):
        for number_3 in range(1, first_number + 1):
            print(f"{number_1} * {number_2} * {number_3} = {number_1 * number_2 * number_3};")
