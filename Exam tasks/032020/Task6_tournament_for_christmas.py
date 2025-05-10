tournament_days: int = int(input())
count_win: int = 0
count_win_total: int = 0
count_lose: int = 0
count_lose_total: int = 0
money_won: float = 0
total_money_won: float = 0

for _ in range(1, tournament_days + 1):

    while True:

        sport: str = input()

        if sport == "Finish":
            money_won = count_win * 20

            if count_win > count_lose:
                money_won *= 1.1

            total_money_won += money_won
            count_win_total += count_win
            count_lose_total += count_lose
            count_win = 0
            count_lose = 0
            money_won = 0
            break

        else:
            result: str = input()

            if result == "win":
                count_win += 1
            elif result == "lose":
                count_lose += 1

if count_win_total > count_lose_total:
    total_money_won *= 1.2
    print(f"You won the tournament! Total raised money: {total_money_won:.2f}")
elif count_lose_total > count_win_total:
    print(f"You lost the tournament! Total raised money: {total_money_won:.2f}")