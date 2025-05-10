time_hours = int(input())
time_minut = int(input())

n_time_minut = time_minut + 15


if n_time_minut >= 60:
    time_hours += 1
    n_time_minut = n_time_minut - 60

if time_hours >= 24:
    time_hours = time_hours % 24

if n_time_minut < 10:
    print(f"{time_hours}:0{n_time_minut}")
else:
    print(f"{time_hours}:{n_time_minut}")
