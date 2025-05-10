number_given: int = int(input())

for number_1 in range(1, 9 + 1):
    for number_2 in range(1, 9 + 1):
        for number_3 in range(1, 9 + 1):
            for number_4 in range(1, 9 + 1):
                sum_first = number_1 + number_2
                sum_second = number_3 + number_4

                if sum_first == sum_second and not number_given % sum_first:

                    print(f"{number_1}{number_2}{number_3}{number_4}", end=" ")
