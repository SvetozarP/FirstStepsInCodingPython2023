a: int = int(input())
b: int = int(input())
number_passwords: int = int(input())

for A in range(35, 55):

    for B in range(64, 96):

        for x in range(1, a + 1):
            for y in range(1, b + 1):

                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")

                number_passwords -= 1
                A += 1
                if A > 55:
                    A = 35
                B += 1
                if B > 96:
                    B = 64

                if number_passwords == 0 or (x == a and y == b):
                    exit(0)
