budget: float = float(input())
count_product: int = 0
total_price: float = 0.00
is_stopped: bool = False
diff: float = 0

while True:

    product: str = input()

    if product == "Stop":
        is_stopped = True
        break

    else:

        prod_price: float = float(input())

        count_product += 1

        if count_product % 3 == 0:
            prod_price = prod_price * 0.5

        total_price += prod_price

        if budget < total_price:
            diff = total_price - budget
            break

if is_stopped:
    print(f"You bought {count_product} products for {total_price:.2f} leva.")

else:
    print("You don't have enough money!")
    print(f"You need {diff:.2f} leva!")
