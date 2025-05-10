from math import floor

ship_width: float = float(input())
ship_length: float = float(input())
ship_height: float = float(input())
avg_height_astro: float = float(input())

ship_volume: float = ship_width * ship_length * ship_height

room_volume: float = (avg_height_astro + 0.4) * 2 * 2

space_available: int = floor(ship_volume / room_volume)

if 3 <= space_available <= 10:
    print(f"The spacecraft holds {space_available} astronauts.")
elif space_available < 3:
    print("The spacecraft is too small.")
elif space_available > 10:
    print("The spacecraft is too big.")
