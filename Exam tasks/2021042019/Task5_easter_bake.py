from sys import maxsize
from math import ceil

number_kozunak: int = int(input())
weight_sugar_pack: int = 950
weight_flour_pack: int = 750

total_sugar_spent: int = 0
total_flour_spent: int = 0


max_sugar: int = -maxsize
max_flour: int = -maxsize

for _ in range(1, number_kozunak + 1):
    sugar_spent: int = int(input())
    flour_spent: int = int(input())

    if sugar_spent > max_sugar:
        max_sugar = sugar_spent

    if flour_spent > max_flour:
        max_flour = flour_spent

    total_flour_spent += flour_spent
    total_sugar_spent += sugar_spent

print(f"Sugar: {ceil(total_sugar_spent / weight_sugar_pack)}")
print(f"Flour: {ceil(total_flour_spent / weight_flour_pack)}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
