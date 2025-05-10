money_need = float(input())
money_have = float(input())

day_counter = 0
spend_counter = 0

while money_have < money_need and spend_counter < 5:
    action = input()
    money = float(input())
    day_counter += 1

    if action == "save":
        money_have += money
        spend_counter = 0
    elif action == "spend":
        money_have -= money
        spend_counter += 1
        if money_have < 0:
            money_have = 0

if spend_counter == 5:
    print("You can't save the money.")
    print(f"{day_counter}")

if money_have >= money_need:
    print(f"You saved the money for {day_counter} days.")
