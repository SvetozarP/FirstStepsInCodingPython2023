steps_achieved = 0
achieved = False

while not achieved:
    more_steps = input()

    if more_steps == "Going home":
        more_steps = int(input())
        steps_achieved += more_steps
        if steps_achieved >= 10000:
            print("Goal reached! Good job!")
            print(f"{steps_achieved - 10000} steps over the goal!")
        elif steps_achieved < 10000:
            print(f"{10000 - steps_achieved} more steps to reach goal.")

        break

    else:
        steps_achieved += int(more_steps)

    if steps_achieved >= 10000:
        achieved = True

if achieved:
    print("Goal reached! Good job!")
    print(f"{steps_achieved - 10000} steps over the goal!")
