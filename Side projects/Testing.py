l_103 = len("103") - 1
sales_str: str = ""
rating_str: str = ""
for index, digit in enumerate("103"):

    if index < l_103:
        sales_str += digit
    elif index == l_103:
        rating_str = digit

print(f"sales:str {sales_str}")
print(f"rating: str {rating_str}")
print(l_103)
