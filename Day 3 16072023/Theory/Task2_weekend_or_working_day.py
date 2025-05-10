day_wk = input()

if day_wk == "Saturday" or day_wk == "Sunday":
    print("Weekend")

elif day_wk == "Monday" or day_wk == "Tuesday" or day_wk == "Wednesday" or day_wk == "Thursday" or day_wk == "Friday":
    print("Working day")

else:
    print("Error")
