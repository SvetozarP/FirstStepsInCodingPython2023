number_km: int = int(input())
time_day: str = input()
price_transport: float = 0.0

if number_km < 20:

    if time_day == "day":
        price_transport = 0.79 * number_km + 0.7
    elif time_day == "night":
        price_transport = 0.9 * number_km + 0.7

elif 20 <= number_km < 100:

    price_transport = number_km * 0.09

elif number_km >= 100:

    price_transport = number_km * 0.06

print(f"{price_transport:.2f}")
