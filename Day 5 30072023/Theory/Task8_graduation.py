name = input()
grade = 1
sum_grades = 0.0
excluded = 0

while grade <= 12:
    grades = float(input())
    if grades < 4:
        excluded += 1
        if excluded > 1:
            print(f"{name} has been excluded at {grade-1} grade")
            break
    sum_grades += grades
    grade += 1
    if grade == 12:
        print(f"{name} graduated. Average grade: {sum_grades / 12:.2f}")



