city = input()
vol_sale = float(input())

if city == "Sofia":

    if 0 <= vol_sale <= 500:
        comiss = 0.05
    elif 500 < vol_sale <= 1000:
        comiss = 0.07
    elif 1000 < vol_sale <= 10000:
        comiss = 0.08
    elif 10000 < vol_sale:
        comiss = 0.12
    else:
        print("error")
        exit(1)

elif city == "Varna":

    if 0 <= vol_sale <= 500:
        comiss = 0.045
    elif 500 < vol_sale <= 1000:
        comiss = 0.075
    elif 1000 < vol_sale <= 10000:
        comiss = 0.1
    elif 10000 < vol_sale:
        comiss = 0.13
    else:
        print("error")
        exit(1)

elif city == "Plovdiv":

    if 0 <= vol_sale <= 500:
        comiss = 0.055
    elif 500 < vol_sale <= 1000:
        comiss = 0.08
    elif 1000 < vol_sale <= 10000:
        comiss = 0.12
    elif 10000 < vol_sale:
        comiss = 0.145
    else:
        print("error")
        exit(1)
else:
    print("error")
    exit(1)

total_comiss = vol_sale * comiss

print(f"{total_comiss:.2f}")
