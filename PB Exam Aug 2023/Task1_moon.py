from math import ceil
average_speed: float = float(input())
fuel_per_hundred: float = float(input())

total_distance: float = 384400 * 2
time_go_and_back: float = total_distance / average_speed

total_time: int = ceil(time_go_and_back) + 3

fuel: float = (fuel_per_hundred * total_distance) / 100

print(f"{total_time}")
print(f"{int(fuel)}")
