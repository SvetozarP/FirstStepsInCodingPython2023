h: float = float(input())
w: float = float(input())

w_to_cm = w * 100
h_to_cm = h * 100

w_to_cm -= 100

total_per_columns: float = w_to_cm // 70
total_columns: float = h_to_cm // 120

total_spaces = total_per_columns * total_columns - 3

print(f"{int(total_spaces)}")
