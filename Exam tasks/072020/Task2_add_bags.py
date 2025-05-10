price_luggage_over_20: float = float(input())
luggage_kg: float = float(input())
days_travel: int = int(input())
count_luggage: int = int(input())

if luggage_kg < 10:
    price_luggage_over_20 *= 0.2
elif 10 <= luggage_kg <= 20:
    price_luggage_over_20 *= 0.5

if days_travel > 30:
    price_luggage_over_20 *= 1.1
elif 7 <= days_travel <= 30:
    price_luggage_over_20 *= 1.15
elif days_travel < 7:
    price_luggage_over_20 *= 1.4

price_mimi: float = count_luggage * price_luggage_over_20

print(f"The total price of bags is: {price_mimi:.2f} lv. ")
