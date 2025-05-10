hall_rent: float = float(input())

cake_price: float = hall_rent * 0.2
drinks_price: float = cake_price - cake_price * 0.45
animator_price: float = hall_rent / 3

total_price: float = hall_rent + cake_price + drinks_price + animator_price

print(f"{total_price}")
