int_start: int = int(input())
int_end: int = int(input())
magic_number: int = int(input())
counter: int = 0
combinations_found: int = 0

for x in range(int_start, int_end + 1):
    for y in range(int_start, int_end + 1):
        counter += 1
        if x + y == magic_number:
            combinations_found += 1
            print(f"Combination N:{counter} ({x} + {y} = {magic_number})")
            break
    if combinations_found:
        break

if combinations_found == 0:
    print(f"{counter} combinations - neither equals {magic_number}")
