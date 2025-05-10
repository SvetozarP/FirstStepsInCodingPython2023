minutes_walking: int = int(input())
count_walking: int = int(input())
calories_daily: int = int(input())

to_burn_calories: float = calories_daily / 2

calories_burned: int = minutes_walking * count_walking * 5

if calories_burned >= to_burn_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")
