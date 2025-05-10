movie_budget: float = float(input())
budget_updated: float = 0
actor_name: str = ""
actor_cost: float = 0.00
budget_over: bool = False

while True:

    actor_name = input()

    if actor_name == "ACTION":
        break

    if len(actor_name) > 15:
        actor_cost = (movie_budget - budget_updated) * 0.2
        budget_updated += actor_cost

    else:
        actor_cost = float(input())
        budget_updated += actor_cost

    if budget_updated > movie_budget:
        budget_over = True
        break

diff = abs(movie_budget - budget_updated)

if budget_over:
    print(f"We need {diff:.2f} leva for our actors.")
else:
    print(f"We are left with {diff:.2f} leva.")
