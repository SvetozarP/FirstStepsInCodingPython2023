upper_first = int(input())
upper_second = int(input())
upper_third = int(input())
not_prime: bool = False

if upper_second > 7:
    upper_second = 7

for number1 in range(1, upper_first + 1):
    for number2 in range(2, upper_second + 1):
        not_prime = False
        for i in range(2, number2):
            if (number2 % i) == 0:
                not_prime = True
        for number3 in range(1, upper_third + 1):

            if not number1 % 2 and not number3 % 2 and not not_prime:
                print(f"{number1} {number2} {number3}")
