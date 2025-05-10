money_needed = float(input())
money_have = float(input())
count_spend = 0
count_saved = 0
money_action = 0
money_saved = 0
last_action = 0
total_days = 0
success = False


while money_saved + money_have < money_needed:
    action = input()
    money_action = float(input())
    total_days += 1
    if action == "save":
        last_action = action
        count_saved += 1
        money_saved += money_action
    elif action == "spend":
        last_action = "spend"
        if money_saved >= money_action:
            money_saved -= money_action
        elif money_saved < money_action:
            money_saved = 0
    if last_action == "spend" and action == "spend":
        count_spend += 1
    elif action == "save":
        count_spend = 0
    if count_spend == 5:
        print("You can't save the money.")
        print(f"{total_days}")
        break
    if money_saved + money_have >= money_needed:
        success = True

if success:
    print(f"You saved the money for {total_days} days.")
