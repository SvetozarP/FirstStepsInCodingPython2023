from math import ceil

n_people = int(input())
entry_fee = float(input())
price_longue = float(input())
price_umbrella = float(input())



need_longue = n_people * 0.75
need_longue = ceil (need_longue)
need_umbrella = n_people / 2
need_umbrella = ceil(need_umbrella)

price_final = need_longue * price_longue + need_umbrella * price_umbrella + n_people * entry_fee

print(f"{price_final:.2f} lv.")