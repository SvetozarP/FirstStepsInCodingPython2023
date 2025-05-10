first_result: str = input()
second_result: str = input()
third_result: str = input()
games_won: int = 0
games_lost: int = 0
games_draw: int = 0

first_result_home, first_result_away = first_result.split(":")
second_result_home, second_result_away = second_result.split(":")
third_result_home, third_result_away = third_result.split(":")

if first_result_home > first_result_away:
    games_won += 1
elif first_result_home == first_result_away:
    games_draw += 1
elif first_result_home < first_result_away:
    games_lost += 1

if second_result_home > second_result_away:
    games_won += 1
elif second_result_home == second_result_away:
    games_draw += 1
elif second_result_home < second_result_away:
    games_lost += 1

if third_result_home > third_result_away:
    games_won += 1
elif third_result_home == third_result_away:
    games_draw += 1
elif third_result_home < third_result_away:
    games_lost += 1

print(f"Team won {games_won} games.")
print(f"Team lost {games_lost} games.")
print(f"Drawn games: {games_draw}")
