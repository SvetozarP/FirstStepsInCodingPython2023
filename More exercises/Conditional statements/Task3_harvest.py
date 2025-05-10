from math import floor
from math import ceil

area_grapes: int = int(input())
grapes_per_sq_m: float = float(input())
wine_needed: int = int(input())
workers_count: int = int(input())

grapes_harvested: float = grapes_per_sq_m * area_grapes
grapes_for_wine: float = grapes_harvested * 0.4
wine_produced: float = grapes_for_wine / 2.5

diff = abs(wine_needed - wine_produced)

if wine_produced < wine_needed:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
elif wine_produced >= wine_needed:
    print(f"Good harvest this year! Total wine: {floor(wine_produced)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(diff / workers_count)} liters per person.")
