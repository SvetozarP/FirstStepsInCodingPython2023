number_cats: int = int(input())
number_group_one: int = 0
number_group_two: int = 0
number_group_three: int = 0
total_food: float = 0.0
food_price_kg: float = 12.45
food_price_day: float = 0.0

for cat in range(number_cats):

    eaten_food: float = float(input())

    if 100 <= eaten_food < 200:
        number_group_one += 1
        total_food += eaten_food
    elif 200 <= eaten_food < 300:
        number_group_two += 1
        total_food += eaten_food
    elif 300 <= eaten_food < 400:
        number_group_three += 1
        total_food += eaten_food

food_price_day = total_food / 1000 * food_price_kg

print(f"Group 1: {number_group_one} cats.")
print(f"Group 2: {number_group_two} cats.")
print(f"Group 3: {number_group_three} cats.")
print(f"Price for food per day: {food_price_day:.2f} lv.")
