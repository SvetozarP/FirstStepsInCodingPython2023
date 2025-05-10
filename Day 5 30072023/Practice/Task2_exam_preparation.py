failed_grades = int(input())
number_problems = 0
num_failed_grades = 0
total_grades = 0
last_task = 0
task_name = input()
has_failed = False

while task_name != "Enough":
    grade = int(input())
    if grade <= 4:
        num_failed_grades += 1
        total_grades += grade
    else:
        number_problems += 1
        total_grades += grade

    if failed_grades == num_failed_grades:
        has_failed = True
        break
    last_task = task_name
    task_name = input()


if has_failed:
    print(f"You need a break, {num_failed_grades} poor grades.")
else:
    avg_score = total_grades / (number_problems + num_failed_grades)
    total_solutions = num_failed_grades + number_problems

    print(f"Average score: {avg_score:.2f}")
    print(f"Number of problems: {total_solutions}")
    print(f"Last problem: {last_task}")
