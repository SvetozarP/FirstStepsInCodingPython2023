from math import floor, ceil

count_magnolia: int = int(input())
count_ziumbiul: int = int(input())
count_rose: int = int(input())
count_cactus: int = int(input())
price_present: float = float(input())

cost_magnolia: float = count_magnolia * 3.25
cost_ziumbiul: float = count_ziumbiul * 4
cost_rose: float = count_rose * 3.5
cost_cactus: float = count_cactus * 8

total_money: float = (cost_magnolia + cost_ziumbiul + cost_rose + cost_cactus) * 0.95

diff = abs(total_money - price_present)

if price_present <= total_money:
    print(f"She is left with {floor(diff)} leva.")
elif price_present > total_money:
    print(f"She will have to borrow {ceil(diff)} leva.")
