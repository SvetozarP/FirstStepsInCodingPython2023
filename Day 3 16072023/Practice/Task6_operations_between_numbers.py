num1 = int(input())
num2 = int(input())
oper = input()
result = 0
iseven = 0

if oper == "+":
    result = num1 + num2
elif oper == "-":
    result = num1 - num2
elif oper == "*":
    result = num1 * num2

if oper == "+" or oper == "-" or oper == "*":
    if result % 2 == 0:
        iseven = "even"
    else:
        iseven = "odd"
    print(f"{num1} {oper} {num2} = {result} - {iseven}")
elif oper == "/":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
        exit(0)
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.2f}")
elif oper == "%":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
        exit(0)
    else:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
