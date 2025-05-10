number_doctors: int = 7
period_to_calc: int = int(input())
treated_patients: int = 0
untreated_patients: int = 0

for day in range(1, period_to_calc + 1):

    if not day % 3:
        if untreated_patients > treated_patients:
            number_doctors += 1

    number_patients: int = int(input())

    if number_patients >= number_doctors:
        treated_patients += number_doctors
        untreated_patients += (number_patients - number_doctors)
    else:
        treated_patients += number_patients

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
