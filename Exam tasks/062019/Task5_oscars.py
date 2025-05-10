actor_name = input()
academy_points = float(input())
no_judges = int(input())

for i in range(1, no_judges+1):
    judges_name = input()
    j_points = float(input())
    name_points = len(judges_name)
    academy_points += name_points * j_points / 2
    if academy_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break

if academy_points <= 1250.5:
    print(f"Sorry, {actor_name} you need {1250.5 - academy_points:.1f} more!")
