minutes_control: int = int(input())
seconds_control: int = int(input())
length_slope: float = float(input())
seconds_per_hundred: int = int(input())

min_to_sec_control = minutes_control * 60
total_control = min_to_sec_control + seconds_control
time_racing = length_slope / 100 * seconds_per_hundred
time_delay = length_slope / 120 * 2.5
total_racing_time = time_racing - time_delay

if total_control >= total_racing_time:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_racing_time:.3f}.")
elif total_control < total_racing_time:
    print(f"No, Marin failed! He was {abs(total_control - total_racing_time):.3f} second slower.")
