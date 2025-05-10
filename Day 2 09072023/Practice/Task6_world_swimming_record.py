from math import floor

record_sec = float(input())
distance_meters = float(input())
sec_per_meter = float(input())

delay_sec = floor(distance_meters / 15) * 12.5
total_swim_no_delay_time = distance_meters * sec_per_meter
total_swim_time = total_swim_no_delay_time + delay_sec

if record_sec <= total_swim_time:
    time_needed = total_swim_time - record_sec
    print(f"No, he failed! He was {time_needed:.2f} seconds slower.")

else:
    time_exceed = total_swim_time
    print(f"Yes, he succeeded! The new world record is {time_exceed:.2f} seconds.")
