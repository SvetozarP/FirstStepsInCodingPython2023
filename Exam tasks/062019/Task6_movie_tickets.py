a1: int = int(input())
a2: int = int(input())
n: int = int(input())

for character in range(a1, a2):

    if character % 2 == 1:
        sym1 = chr(character)

        for character1 in range(1, n):
            for character2 in range(1, int(n/2)):

                if (character1 + character2 + ord(sym1)) % 2 == 1:
                    print(f"{sym1}-{character1}{character2}{ord(sym1)}")
