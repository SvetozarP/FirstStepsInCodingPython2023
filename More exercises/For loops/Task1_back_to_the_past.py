inherited_money: float = float(input())
year_life: int = int(input())

for year in range(1800, year_life + 1):

    if not year % 2:
        inherited_money -= 12000
    if year % 2:
        inherited_money -= 12000 + 50 * (year - 1800 + 18)

if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
else:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")
