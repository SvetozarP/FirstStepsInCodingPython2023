while True:

    number: float = float(input())
    result: float = 0.0

    if number < 0:
        print("Negative number!")
        break
    else:
        result = number * 2
        print(f"Result: {result:.2f}")
