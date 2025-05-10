n: int = int(input())
l: int = int(input())
start_letter: int = ord("a")
end_letter: int = start_letter + l

for first_num in range(1, n):
    for second_num in range(1, n):
        for first_letter in range(start_letter, end_letter):
            for second_letter in range(start_letter, end_letter):
                for third_num in range(1, n + 1):

                    if third_num > first_num and third_num > second_num:
                        print(f"{first_num}{second_num}{chr(first_letter)}{chr(second_letter)}{third_num}", end=" ")
