price_veg_kg: float = float(input())
price_fruit_kg: float = float(input())
kg_veg: int = int(input())
kg_fruit: int = int(input())

total_price_lv: float = price_veg_kg * kg_veg + price_fruit_kg * kg_fruit
total_price: float = total_price_lv / 1.94

print(f"{total_price:.2f}")
