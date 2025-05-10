number_adults: int = 0
number_kids: int = 0
price_toy: int = 5
price_pullover: int = 15
years_member_n: int = 0
money_toy: int = 0
money_pullover: int = 0

while True:

    years_member: str = input()

    if years_member == "Christmas":

        money_toy = number_kids * price_toy
        money_pullover = number_adults * price_pullover

        print(f"Number of adults: {number_adults}")
        print(f"Number of kids: {number_kids}")
        print(f"Money for toys: {money_toy}")
        print(f"Money for sweaters: {money_pullover}")
        break

    else:
        years_member_n = int(years_member)

        if years_member_n <= 16:
            number_kids += 1
        elif years_member_n > 16:
            number_adults += 1
