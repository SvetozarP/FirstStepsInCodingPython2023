number_customers: int = int(input())
total_purchase: int = 0
current_customer_purchase: int = 0
discount: float = 1.00
customer_cost: float = 0
total_cost: float = 0

for _ in range(1, number_customers + 1):

    while True:
        purchase: str = input()

        if purchase == "Finish":
            break

        if purchase == "basket":
            customer_cost += 1.5
            current_customer_purchase += 1
        elif purchase == "wreath":
            customer_cost += 3.8
            current_customer_purchase += 1
        elif purchase == "chocolate bunny":
            customer_cost += 7
            current_customer_purchase += 1

    if current_customer_purchase % 2 == 0:
        customer_cost *= 0.8

    print(f"You purchased {current_customer_purchase} items for {customer_cost:.2f} leva.")
    total_cost += customer_cost
    customer_cost = 0
    current_customer_purchase = 0

print(f"Average bill per client is: {total_cost / number_customers:.2f} leva.")
