name_of_counry: str = input()
competition_tool: str = input()
score_difficulty: float = 0.00
score_performance: float = 0.00
total_score: float = 0.00
score_remain: float = 0.00
percent_needed: float = 0.00

if name_of_counry == "Russia":

    if competition_tool == "ribbon":

        score_difficulty = 9.1
        score_performance = 9.4
        total_score = score_difficulty + score_performance

    elif competition_tool == "hoop":

        score_difficulty = 9.3
        score_performance = 9.8
        total_score = score_difficulty + score_performance

    elif competition_tool == "rope":

        score_difficulty = 9.6
        score_performance = 9.0
        total_score = score_difficulty + score_performance

elif name_of_counry == "Bulgaria":

    if competition_tool == "ribbon":

        score_difficulty = 9.6
        score_performance = 9.4
        total_score = score_difficulty + score_performance

    elif competition_tool == "hoop":

        score_difficulty = 9.55
        score_performance = 9.75
        total_score = score_difficulty + score_performance

    elif competition_tool == "rope":

        score_difficulty = 9.5
        score_performance = 9.4
        total_score = score_difficulty + score_performance

elif name_of_counry == "Italy":

    if competition_tool == "ribbon":

        score_difficulty = 9.2
        score_performance = 9.5
        total_score = score_difficulty + score_performance

    elif competition_tool == "hoop":

        score_difficulty = 9.45
        score_performance = 9.35
        total_score = score_difficulty + score_performance

    elif competition_tool == "rope":

        score_difficulty = 9.7
        score_performance = 9.15
        total_score = score_difficulty + score_performance

score_remain = 20 - total_score
percent_needed = (score_remain / 20) * 100

print(f"The team of {name_of_counry} get {total_score:.3f} on {competition_tool}.")
print(f"{percent_needed:.2f}%")
