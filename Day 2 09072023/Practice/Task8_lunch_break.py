from math import ceil

name_series = input()
time_episode = int(input())
time_break = int(input())

time_lunch = time_break * 1/8
time_relax = time_break * 1/4

time_for_series = time_break - time_lunch - time_relax

if time_episode < time_for_series:
    time_left = ceil(time_for_series - time_episode)
    print(f"You have enough time to watch {name_series} and left with {time_left} minutes free time.")

else:
    time_needed = ceil(time_episode - time_for_series)
    print(f"You don't have enough time to watch {name_series}, you need {time_needed} more minutes.")
