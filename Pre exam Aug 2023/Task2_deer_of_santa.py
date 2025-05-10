from math import floor, ceil

days_absence: int = int(input())
feed_kg: int = int(input())
feed_1st_deer: float = float(input())
feed_2nd_deer: float = float(input())
feed_3rd_deer: float = float(input())

feed_need_1st: float = days_absence * feed_1st_deer
feed_need_2nd: float = days_absence * feed_2nd_deer
feed_need_3rd: float = days_absence * feed_3rd_deer

total_feed_need: float = feed_need_1st + feed_need_2nd + feed_need_3rd

if feed_kg >= total_feed_need:

    print(f"{floor(feed_kg - total_feed_need)} kilos of food left.")

if feed_kg < total_feed_need:

    print(f"{ceil(total_feed_need - feed_kg)} more kilos of food are needed.")
