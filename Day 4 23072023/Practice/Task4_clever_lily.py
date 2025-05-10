lily_age = int(input())
washer_price = float(input())
price_toy = int(input())
number_toys = 0
money_saved = 0
count_days = 0

for i in range(1, lily_age + 1):
    if i % 2 == 0:
        count_days += 1
        money_saved += count_days * 10
    else:
        number_toys += 1

toys_price = number_toys * price_toy
money_total = money_saved + toys_price - count_days
money_diff = abs(washer_price - money_total)

if washer_price <= money_total:
    print(f"Yes! {money_diff:.2f}")
if washer_price > money_total:
    print(f"No! {money_diff:.2f}")
