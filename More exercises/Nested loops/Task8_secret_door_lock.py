upper_limit_h: int = int(input())
upper_limit_d: int = int(input())
upper_limit_n: int = int(input())
not_prime: bool = False

for hundreds in range(1, upper_limit_h + 1):
    for dec in range(1, upper_limit_d + 1):
        for number in range(1, upper_limit_n + 1):

            if not hundreds % 2 and not number % 2 and 2 <= dec <= 7:

                for i in range(2, dec):
                    if (dec % i) == 0:
                        not_prime = True

                if not not_prime:
                    print(f"{hundreds} {dec} {number}")
                not_prime = False
