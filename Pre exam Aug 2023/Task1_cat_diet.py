fat_percentage: int = int(input())
protein_percentage: int = int(input())
carb_percentage: int = int(input())
total_calories: int = int(input())
water_content: int = int(input())

grams_fat: float = (fat_percentage / 100 * total_calories) / 9
grams_protein: float = (protein_percentage / 100 * total_calories) / 4
grams_carb: float = (carb_percentage / 100 * total_calories) / 4

total_grams: float = grams_fat + grams_protein + grams_carb

cal_per_gr: float = total_calories / total_grams

grams_without_water = cal_per_gr - cal_per_gr * water_content / 100

print(f"{grams_without_water:.4f}")
