price_flour: float = float(input())
amount_flour: float = float(input())
amount_sugar: float = float(input())
count_egg_packs: int = int(input())
packs_yeast: int = int(input())

price_sugar = price_flour * 0.75
price_egg_pack = price_flour * 1.1
price_yeast = price_sugar * 0.2

total_price = price_flour * amount_flour + price_sugar * amount_sugar + count_egg_packs * price_egg_pack + \
              packs_yeast * price_yeast

print(f"{total_price:.2f}")
