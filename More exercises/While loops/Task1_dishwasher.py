number_bottles: int = int(input())
qty_detergent: int = number_bottles * 750
count_washes: int = 0
count_pots: int = 0
count_dishes: int = 0

while True:

    to_wash: str = input()

    if to_wash == "End":
        print("Detergent was enough!")
        print(f"{count_dishes} dishes and {count_pots} pots were washed.")
        print(f"Leftover detergent {qty_detergent} ml.")
        break

    else:

        to_wash_int = int(to_wash)
        count_washes += 1

        if count_washes % 3 == 0:

            qty_detergent -= to_wash_int * 15
            count_pots += to_wash_int
        else:

            qty_detergent -= to_wash_int * 5
            count_dishes += to_wash_int

        if qty_detergent < 0:

            print(f"Not enough detergent, {abs(qty_detergent)} ml. more necessary!")
            break
