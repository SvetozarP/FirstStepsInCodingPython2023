name_student = input()
exam_passed = 0
exam_failed = 0
total_grades = 0

while exam_passed < 12 and exam_failed < 2:
    grade = float(input())

    if grade >= 4:
        exam_passed += 1
        total_grades += grade
    else:
        exam_failed += 1
    if exam_passed == 12:
        print(f"{name_student} graduated. Average grade: {total_grades / 12:.2f}")
        break
    if exam_failed == 2:
        print(f"{name_student} has been excluded at {exam_passed + 1} grade")
        break
