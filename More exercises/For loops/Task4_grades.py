number_students: int = int(input())
count_top: int = 0
count_4: int = 0
count_3: int = 0
count_fail: int = 0
sum_grades: float = 0.0
average_grade: float = 0.0

for _ in range(1, number_students + 1):

    student_grade: float = float(input())

    if 2 <= student_grade <= 2.99:
        count_fail += 1
        sum_grades += student_grade
    elif 3 <= student_grade <= 3.99:
        count_3 += 1
        sum_grades += student_grade
    elif 4 <= student_grade <= 4.99:
        count_4 += 1
        sum_grades += student_grade
    elif student_grade >= 5:
        count_top += 1
        sum_grades += student_grade

average_grade = sum_grades / (count_fail + count_3 + count_4 + count_top)

print(f"Top students: {count_top / number_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {count_4 / number_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {count_3 / number_students * 100:.2f}%")
print(f"Fail: {count_fail / number_students * 100:.2f}%")
print(f"Average: {average_grade:.2f}")
