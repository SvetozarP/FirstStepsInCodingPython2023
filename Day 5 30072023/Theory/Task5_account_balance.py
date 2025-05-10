text_input = input()
money_total = 0


while text_input != "NoMoreMoney":
    money_in = float(text_input)
    if money_in >= 0:
        print(f"Increase: {money_in:.2f}")
        money_total += money_in
        text_input = input()
    else:
        print("Invalid operation!")
        break

print(f"Total: {money_total:.2f}")
