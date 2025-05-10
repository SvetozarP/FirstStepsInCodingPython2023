finished: bool = False
sum_to_add: float = 0

while not finished:
    destination: str = input()

    if destination != "End":

        min_budget: float = float(input())
        total_money: float = 0.00

        while total_money <= min_budget:
            sum_to_add: str = input()

            if sum_to_add != "End":
                total_money += float(sum_to_add)

                if total_money >= min_budget:
                    total_money = 0
                    print(f"Going to {destination}!")
                    break

            elif sum_to_add == "End":
                finished = True
                print(f"Going to {destination}!")
                exit(0)

    elif destination == "End":
        finished = True
