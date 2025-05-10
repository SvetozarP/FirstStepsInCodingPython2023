fr_type = input()
day_wk = input()
qty = float(input())
price = 0

if day_wk == "Monday" or day_wk == "Tuesday" or day_wk == "Wednesday" or day_wk == "Thursday" or day_wk == "Friday":

    if fr_type == "banana":
        price = 2.5
    elif fr_type == "apple":
        price = 1.2
    elif fr_type == "orange":
        price = 0.85
    elif fr_type == "grapefruit":
        price = 1.45
    elif fr_type == "kiwi":
        price = 2.7
    elif fr_type == "pineapple":
        price = 5.5
    elif fr_type == "grapes":
        price = 3.85
    else:
        print("error")
        exit(1)

elif day_wk == "Saturday" or day_wk == "Sunday":

    if fr_type == "banana":
        price = 2.7
    elif fr_type == "apple":
        price = 1.25
    elif fr_type == "orange":
        price = 0.9
    elif fr_type == "grapefruit":
        price = 1.6
    elif fr_type == "kiwi":
        price = 3
    elif fr_type == "pineapple":
        price = 5.6
    elif fr_type == "grapes":
        price = 4.2
    else:
        print("error")
        exit(1)
else:
    print("error")
    exit(1)

total_price = qty * price
print(f"{total_price:.2f}")