x1: float = float(input())
y1: float = float(input())
x2: float = float(input())
y2: float = float(input())
x: float = float(input())
y: float = float(input())

if (x == x1 or x == x2) and y1 <= y <= y2:

    print("Border")

elif (y == y1 or y == y2) and x1 <= x <= x2:

    print("Border")

else:

    print("Inside / Outside")
