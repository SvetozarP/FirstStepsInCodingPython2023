jury_count: int = int(input())
presentation_name: str = input()
total_grades = 0
avg_grade = 0
count_presentations = 0
grade_per_presentation = 0
total_avg = 0

while presentation_name != "Finish":

    for i in range(0, jury_count):
        sum_grade: float = float(input())
        grade_per_presentation += sum_grade

    avg_grade = grade_per_presentation / jury_count
    total_grades += grade_per_presentation
    print(f"{presentation_name} - {avg_grade:.2f}.")
    grade_per_presentation = 0
    count_presentations += 1
    presentation_name: str = input()

total_avg = total_grades / count_presentations / jury_count

print(f"Student's final assessment is {total_avg:.2f}.")
