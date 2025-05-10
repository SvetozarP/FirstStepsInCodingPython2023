from math import floor, ceil

days_absence: int = int(input())
feed_in_kg: int = int(input())
dog_feed_kg_day: float = float(input())
cat_feed_kg_day: float = float(input())
tort_feed_gr_day: float = float(input())
tort_feed_kg_day: float = tort_feed_gr_day / 1000

dog_ate: float = dog_feed_kg_day * days_absence
cat_ate: float = cat_feed_kg_day * days_absence
tort_ate: float = tort_feed_kg_day * days_absence

total_eaten: float = dog_ate + cat_ate + tort_ate

diff = abs(feed_in_kg - total_eaten)

if total_eaten <= feed_in_kg:
    print(f"{floor(diff)} kilos of food left.")
elif total_eaten > feed_in_kg:
    print(f"{ceil(diff)} more kilos of food are needed.")
