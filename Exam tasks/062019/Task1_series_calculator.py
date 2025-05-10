from math import floor

name_series = input()
no_seasons = int(input())
no_episodes = int(input())
time_episod_no_ad = float(input())
total_episode_time = time_episod_no_ad + time_episod_no_ad * 0.2
extra_time = no_seasons * 10

total_time = no_seasons * no_episodes * total_episode_time + extra_time

total_time = floor(total_time)

print(f"Total time needed to watch the {name_series} series is {total_time} minutes.")
