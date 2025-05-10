expected_sum: int = int(input())
counter: int = 0
paid_cs: int = 0
paid_cc: int = 0
counter_cs: int = 0
counter_cc: int = 0

while True:

    currentinput: str = input()
    counter += 1

    if currentinput == "End":
        print("Failed to collect required money for charity.")
        break

    price_item: int = int(currentinput)

    if counter % 2 == 1:

        if price_item > 100:
            print("Error in transaction!")
            continue
        elif price_item <= 100:
            paid_cs += price_item
            counter_cs += 1
            expected_sum -= price_item
            print("Product sold!")

    elif counter % 2 == 0:

        if price_item < 10:
            print("Error in transaction!")
            continue
        elif price_item >= 10:
            paid_cc += price_item
            counter_cc += 1
            expected_sum -= price_item
            print("Product sold!")

    if expected_sum <= 0:
        print(f"Average CS: {paid_cs / counter_cs:.2f}")
        print(f"Average CC: {paid_cc / counter_cc:.2f}")
        break
