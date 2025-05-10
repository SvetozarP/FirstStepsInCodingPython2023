budget: float = float(input())
category: str = input()
group_size: int = int(input())
price_ticket: float = 0.0
transport_cost: float = 0.0

if category == "VIP":
    price_ticket = 499.99

elif category == "Normal":

    price_ticket = 249.99

if 1 <= group_size <= 4:
    transport_cost = budget * 0.75
elif 5 <= group_size <= 9:
    transport_cost = budget * 0.6
elif 10 <= group_size <= 24:
    transport_cost = budget * 0.5
elif 25 <= group_size <= 49:
    transport_cost = budget * 0.4
elif group_size >= 50:
    transport_cost = budget * 0.25

total_cost: float = price_ticket * group_size + transport_cost

diff = abs(total_cost - budget)

if budget >= total_cost:
    print(f"Yes! You have {diff:.2f} leva left.")
elif budget < total_cost:
    print(f"Not enough money! You need {diff:.2f} leva.")
