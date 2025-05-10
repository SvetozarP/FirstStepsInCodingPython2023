hour_day = int(input())
day_wk = input()

if hour_day < 10 or hour_day > 18 or day_wk == "Sunday":
    print("closed")

else:
    print("open")