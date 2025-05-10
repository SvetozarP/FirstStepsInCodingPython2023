count_sea_excursions: int = int(input())
count_mountain_excursions: int = int(input())
sold_sea: int = 0
sold_mountain: int = 0

while True:

    type_exc: str = input()

    if type_exc == "Stop":
        profit_sea: int = sold_sea * 680
        profit_mountain: int = sold_mountain * 499
        break

    if type_exc == "sea" and count_sea_excursions > 0:
        count_sea_excursions -= 1
        sold_sea += 1
    elif type_exc == "mountain" and count_mountain_excursions > 0:
        count_mountain_excursions -= 1
        sold_mountain += 1

    if count_sea_excursions == 0 and count_mountain_excursions == 0:

        print(f"Good job! Everything is sold.")
        profit_sea: int = sold_sea * 680
        profit_mountain: int = sold_mountain * 499
        break

total_profit: int = profit_sea + profit_mountain

print(f"Profit: {total_profit} leva.")
