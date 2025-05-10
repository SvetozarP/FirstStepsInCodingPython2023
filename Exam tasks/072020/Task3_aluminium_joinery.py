count_windows: int = int(input())
type_windows: str = input()
delivery: str = input()
price_single: float = 0.00
total_cost: float = 0.00

if count_windows < 10:
    print(f"Invalid order")
    exit(0)

elif type_windows == "90X130":

    price_single = 110
    total_cost = price_single * count_windows

    if 30 < count_windows <= 60:
        total_cost *= 0.95
    elif count_windows > 60:
        total_cost *= 0.92

elif type_windows == "100X150":

    price_single = 140
    total_cost = price_single * count_windows

    if 40 < count_windows <= 80:
        total_cost *= 0.94
    elif count_windows > 80:
        total_cost *= 0.90

elif type_windows == "130X180":

    price_single = 190
    total_cost = price_single * count_windows

    if 20 < count_windows <= 50:
        total_cost *= 0.93
    elif count_windows > 50:
        total_cost *= 0.88

elif type_windows == "200X300":

    price_single = 250
    total_cost = price_single * count_windows

    if 25 < count_windows <= 50:
        total_cost *= 0.91
    elif count_windows > 50:
        total_cost *= 0.86

if delivery == "With delivery":
    total_cost += 60

if count_windows > 99:
    total_cost *= 0.96

print(f"{total_cost:.2f} BGN")
