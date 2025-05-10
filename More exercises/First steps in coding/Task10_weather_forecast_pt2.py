degrees_c: float = float(input())

if 5 <= degrees_c <= 11.9:
    print("Cold")
elif 12 <= degrees_c <= 14.9:
    print("Cool")
elif 15 <= degrees_c <= 20:
    print("Mild")
elif 20.1 <= degrees_c <= 25.9:
    print("Warm")
elif 26 <= degrees_c <= 35:
    print("Hot")
else:
    print("unknown")
