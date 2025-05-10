from math import floor

record_seconds: float = float(input())
distance_meters: float = float(input())
time_per_meter: float = float(input())

seconds_due_to_slope: int = floor(distance_meters / 50) * 30
time_unslowed: float = time_per_meter * distance_meters

time_slowed: float = time_unslowed + seconds_due_to_slope

if record_seconds > time_slowed:
    print(f"Yes! The new record is {time_slowed:.2f} seconds.")
else:
    print(f"No! He was {abs(record_seconds - time_slowed):.2f} seconds slower.")
