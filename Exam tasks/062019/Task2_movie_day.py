filming_time = int(input())
no_scenes = int(input())
time_per_scene = int(input())
extra_time = filming_time * 0.15

total_time = no_scenes * time_per_scene + extra_time

if filming_time >= total_time:
    time_left = filming_time - total_time
    print(f"You managed to finish the movie on time! You have {round(time_left)} minutes left!")

elif filming_time < total_time:
    time_need = total_time - filming_time
    print(f"Time is up! To complete the movie you need {round(time_need)} minutes.")
