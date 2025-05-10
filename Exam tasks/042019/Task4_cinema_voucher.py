voucher_value: int = int(input())
cost_lubo: int = 0
count_purchase_ticket: int = 0
count_purchase: int = 0

while cost_lubo <= voucher_value:

    name_purchase: str = input()

    if name_purchase == "End":
        break

    elif len(name_purchase) > 8:

        for index, digit in enumerate(name_purchase):

            if index == 0:
                cost_lubo += ord(digit)

            elif index == 1:
                cost_lubo += ord(digit)

        if cost_lubo <= voucher_value:

            count_purchase_ticket += 1

    elif len(name_purchase) <= 8:

        for index, digit in enumerate(name_purchase):

            if index == 0:
                cost_lubo += ord(digit)

        if cost_lubo <= voucher_value:
            count_purchase += 1

print(f"{count_purchase_ticket}")
print(f"{count_purchase}")
