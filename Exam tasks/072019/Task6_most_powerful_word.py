from math import floor
from sys import maxsize
multi_length: bool = False
max_size: int = -maxsize
point_word: int = 0
win_word: str = ""

while True:
    word: str = input()
    len_word: int = len(word)

    if word == "End of words":
        break

    else:

        for index, digit in enumerate(word):

            point_word += ord(digit)

            if index == 0:

                if digit == "a" or digit == "e" or digit == "i" or digit == "o" or digit == "u" or digit == "y" or \
                        digit == "A" or digit == "E" or digit == "I" or digit == "O" or digit == "U" or digit == "Y":

                    multi_length = True

        if multi_length:
            point_word = point_word * len_word
        else:
            point_word = floor(point_word / len_word)

        if point_word > max_size:
            win_word = word
            max_size = point_word

    point_word = 0
    multi_length = False

print(f"The most powerful word is {win_word} - {max_size}")
