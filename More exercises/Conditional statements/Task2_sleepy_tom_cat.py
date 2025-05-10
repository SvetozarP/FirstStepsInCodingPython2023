rest_days: int = int(input())
work_days: int = 365 - rest_days

play_rest_days: int = rest_days * 127
play_work_days: int = work_days * 63

total_play_minutes: int = play_work_days + play_rest_days

tom_norm_play = 30000

diff = abs(tom_norm_play - total_play_minutes)
diff_h = diff // 60
diff_m = diff % 60

if total_play_minutes > tom_norm_play:
    print(f"Tom will run away")
    print(f"{diff_h} hours and {diff_m} minutes more for play")
elif total_play_minutes <= tom_norm_play:
    print(f"Tom sleeps well")
    print(f"{diff_h} hours and {diff_m} minutes less for play")
