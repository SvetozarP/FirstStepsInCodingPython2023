from sys import maxsize

number_eggs: int = int(input())

number_red: int = 0
number_orange: int = 0
number_blue: int = 0
number_green: int = 0
max_eggs: int = -maxsize
max_colour: str = ""

for _ in range(1, number_eggs + 1):

    colour_egg: str = input()

    if colour_egg == "red":
        number_red += 1

        if number_red > max_eggs:
            max_eggs = number_red
            max_colour = "red"

    elif colour_egg == "orange":
        number_orange += 1

        if number_orange > max_eggs:
            max_eggs = number_orange
            max_colour = "orange"

    elif colour_egg == "blue":
        number_blue += 1

        if number_blue > max_eggs:
            max_eggs = number_blue
            max_colour = "blue"

    elif colour_egg == "green":
        number_green += 1

        if number_green > max_eggs:
            max_eggs = number_green
            max_colour = "green"

print(f"Red eggs: {number_red}")
print(f"Orange eggs: {number_orange}")
print(f"Blue eggs: {number_blue}")
print(f"Green eggs: {number_green}")
print(f"Max eggs: {max_eggs} -> {max_colour}")