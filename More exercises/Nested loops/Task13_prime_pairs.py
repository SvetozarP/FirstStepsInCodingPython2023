first_start: int = int(input())
second_start: int = int(input())
first_distance: int = int(input())
second_distance: int = int(input())
first_end: int = first_start + first_distance
second_end: int = second_start + second_distance

for pair in range(first_start, first_end + 1):
    for pair1 in range(second_start, second_end + 1):

        is_prime: bool = True
        is_prime1: bool = True

        for i in range(2, pair):
            if not pair % i:
                is_prime = False
                break

        for j in range(2, pair1):
            if not pair1 % j:
                is_prime1 = False
                break

        if is_prime and is_prime1:
            print(f"{pair}{pair1}")
