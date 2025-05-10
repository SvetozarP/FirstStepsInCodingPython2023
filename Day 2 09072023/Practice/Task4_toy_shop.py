price_vacation = float(input())
count_puzz = int(input())
count_talk_doll = int(input())
count_plush_teddy = int(input())
count_minions = int(input())
count_trucks = int(input())

price_puzz = count_puzz * 2.6
price_talk_doll = count_talk_doll * 3
price_plush_teddy = count_plush_teddy * 4.1
price_minions = count_minions * 8.2
price_trucks = count_trucks * 2

total_toys = count_puzz + count_talk_doll + count_plush_teddy + count_minions + count_trucks
total_price = price_puzz + price_talk_doll + price_plush_teddy + price_minions + price_trucks

if total_toys >= 50:
    discount_price = total_price * 0.25
else:
    discount_price = 0

tot_fin_price = total_price - discount_price
rent = tot_fin_price * 0.1

tot_margin = tot_fin_price - rent

if tot_margin >= price_vacation:
    mon_left = tot_margin - price_vacation
    print(f"Yes! {mon_left:.2f} lv left.")

elif tot_margin < price_vacation:
    mon_need = price_vacation - tot_margin
    print(f"Not enough money! {mon_need:.2f} lv needed.")
