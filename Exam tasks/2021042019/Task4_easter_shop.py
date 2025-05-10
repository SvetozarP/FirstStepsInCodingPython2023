shop_eggs: int = int(input())
eggs_sold: int = 0

while True:

    action_shop: str = input()

    if action_shop == "Close":
        print(f"Store is closed!")
        print(f"{eggs_sold} eggs sold.")
        break

    number_eggs_action: int = int(input())

    if action_shop == "Buy":

        if number_eggs_action > shop_eggs:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {shop_eggs}.")
            break

        shop_eggs -= number_eggs_action
        eggs_sold += number_eggs_action

    elif action_shop == "Fill":

        shop_eggs += number_eggs_action


