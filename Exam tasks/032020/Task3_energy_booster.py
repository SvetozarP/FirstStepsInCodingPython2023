fruit: str = input()
set_size: str = input()
count_sets: int = int(input())

price: float = 0.00

if set_size == "small":

    if fruit == "Watermelon":
        price = 2 * 56 * count_sets
    elif fruit == "Mango":
        price = 2 * 36.66 * count_sets
    elif fruit == "Pineapple":
        price = 2 * 42.1 * count_sets
    elif fruit == "Raspberry":
        price = 2 * 20 * count_sets

elif set_size == "big":

    if fruit == "Watermelon":
        price = 5 * 28.7 * count_sets
    elif fruit == "Mango":
        price = 5 * 19.6 * count_sets
    elif fruit == "Pineapple":
        price = 5 * 24.8 * count_sets
    elif fruit == "Raspberry":
        price = 5 * 15.2 * count_sets

if 400 <= price <= 1000:
    price *= 0.85
elif price > 1000:
    price *= 0.5

print(f"{price:.2f} lv.")
