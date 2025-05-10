number_computers: int = int(input())
sales_str: str = ""
rating_str: str = ""
total_rating: int = 0
total_sales: int = 0

for _ in range(0, number_computers):

    number_rating_sales: str = input()

    length_nrs: int = len(number_rating_sales) - 1

    for index, digit in enumerate(number_rating_sales):

        if index < length_nrs:
            sales_str += digit
        elif index == length_nrs:
            rating_str = digit

    rating: int = int(rating_str)
    sales: int = int(sales_str)

    if rating == 2:
        sales = 0
    elif rating == 3:
        sales *= 0.5
    elif rating == 4:
        sales *= 0.7
    elif rating == 5:
        sales *= 0.85
    elif rating == 6:
        sales = sales

    total_rating += rating
    sales_str = ""
    total_sales += sales
    rating_str = ""

print(f"{total_sales:.2f}")
print(f"{total_rating / number_computers:.2f}")
