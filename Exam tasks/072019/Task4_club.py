wanted_profit: float = float(input())
current_profit: float = 0.00
is_command = False
is_reached = False

while True:

    name_coctail: str = input()

    if name_coctail == "Party!":
        is_command = True
        break

    number_coctail: int = int(input())

    price = len(name_coctail) * number_coctail

    if price % 2 == 1:

        price = price * 0.75

    current_profit += price

    if current_profit >= wanted_profit:
        is_reached = True
        break

    price = 0.00

if is_command:
    print(f"We need {abs(current_profit - wanted_profit):.2f} leva more.")
elif is_reached:
    print("Target acquired.")

print(f"Club income - {current_profit:.2f} leva.")
