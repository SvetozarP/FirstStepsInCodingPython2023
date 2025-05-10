price_strawberries: float = float(input())
qty_bananas_kg: float = float(input())
qty_oranges_kg: float = float(input())
qty_raspberries_kg: float = float(input())
qty_strawberries_kg: float = float(input())

t_price_strawberries = price_strawberries * qty_strawberries_kg
price_raspberries: float = price_strawberries / 2
t_price_raspberries: float = price_raspberries * qty_raspberries_kg
price_oranges: float = price_raspberries * 0.6
t_price_oranges: float = price_oranges * qty_oranges_kg
price_bananas: float = price_raspberries * 0.2
t_price_bananas: float = price_bananas * qty_bananas_kg

total_price: float = t_price_strawberries + t_price_raspberries + t_price_oranges + t_price_bananas

print(f"{total_price:.2f}")
