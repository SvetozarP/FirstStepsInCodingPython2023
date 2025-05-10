found_c: bool = False
found_o: bool = False
found_n: bool = False
word: str = ""
word_to_print: str = ""

while True:
    symbol: str = input()

    if symbol == "End":
        print(word_to_print)
        break

    if symbol == "c" and not found_c:
        found_c = True

    elif symbol == "o" and not found_o:
        found_o = True

    elif symbol == "n" and not found_n:
        found_n = True

    elif symbol.isalpha():
        word += symbol

    if found_c and found_n and found_o:
        word += " "
        word_to_print += word
        found_n = False
        found_o = False
        found_c = False
        word = ""
