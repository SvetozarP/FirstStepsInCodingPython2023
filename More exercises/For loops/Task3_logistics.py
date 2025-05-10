number_loads: int = int(input())
weight_bus: int = 0
weight_truck: int = 0
weight_train: int = 0
total_price: int = 0
avg_price: float = 0.0
total_weight: int = 0

for _ in range(1, number_loads + 1):

    load_weight: int = int(input())

    if load_weight <= 3:
        weight_bus += load_weight
        total_price += load_weight * 200
    elif 4 <= load_weight <= 11:
        weight_truck += load_weight
        total_price += load_weight * 175
    elif load_weight >= 12:
        weight_train += load_weight
        total_price += load_weight * 120

total_weight = weight_bus + weight_train + weight_truck
avg_price = total_price / total_weight

print(f"{avg_price:.2f}")
print(f"{weight_bus / total_weight * 100:.2f}%")
print(f"{weight_truck / total_weight * 100:.2f}%")
print(f"{weight_train / total_weight * 100:.2f}%")
