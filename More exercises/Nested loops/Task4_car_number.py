number_start: int = int(input())
number_end: int = int(input())


for number_1 in range(number_start, number_end + 1):
    for number_2 in range(number_start, number_end + 1):
        for number_3 in range(number_start, number_end + 1):

            sum_2_3: int = number_2 + number_3

            for number_4 in range(number_start, number_end + 1):

                to_print: bool = False

                if (number_1 % 2 == 0 and number_4 % 2 == 1) or (number_1 % 2 == 1 and number_4 % 2 == 0):
                    to_print = True

                if to_print and number_1 > number_4 and not sum_2_3 % 2:
                    print(f"{number_1}{number_2}{number_3}{number_4}", end=" ")
