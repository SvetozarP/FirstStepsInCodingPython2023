number_months: int = int(input())
total_el: float = 0.0
total_wa: int = 0
total_net: int = 0
total_other: int = 0
other_ex: float = 0.0
all_expense: float = 0.0

for _ in range(0, number_months):

    electricity_bill: float = float(input())
    total_el += electricity_bill
    total_wa += 20
    total_net += 15
    other_ex = (electricity_bill + 20 + 15) * 1.2
    total_other += other_ex

all_expense = total_el + total_wa + total_net + total_other

print(f"Electricity: {total_el:.2f} lv")
print(f"Water: {total_wa:.2f} lv")
print(f"Internet: {total_net:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {all_expense / number_months:.2f} lv")
