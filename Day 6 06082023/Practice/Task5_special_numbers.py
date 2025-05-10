number: int = int(input())
is_special = True

for test_number in range(1111, 10000):

    test_n_to_string = str(test_number)

    for index, digit in enumerate(test_n_to_string):

        if int(digit) == 0:
            is_special = False
            break

        elif number % int(digit) == 0:
            is_special = True

        elif number % int(digit) != 0:
            is_special = False
            break

    if is_special:
        print(test_number, end=" ")

    is_special = True
