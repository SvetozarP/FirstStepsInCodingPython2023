letter_start: str = input()
letter_end: str = input()
letter_to_miss: str = input()

letter_start_to_ascii: int = ord(letter_start)
letter_end_to_ascii: int = ord(letter_end)
letter_to_miss_to_ascii: int = ord(letter_to_miss)
counter: int = 0

for ascii_one in range(letter_start_to_ascii, letter_end_to_ascii + 1):
    for ascii_two in range(letter_start_to_ascii, letter_end_to_ascii + 1):
        for ascii_three in range(letter_start_to_ascii, letter_end_to_ascii + 1):

            if ascii_one != letter_to_miss_to_ascii and ascii_two != letter_to_miss_to_ascii and \
                    ascii_three != letter_to_miss_to_ascii:

                print(f"{chr(ascii_one)}{chr(ascii_two)}{chr(ascii_three)}", end=" ")
                counter += 1

print(f"{counter}", end="")
