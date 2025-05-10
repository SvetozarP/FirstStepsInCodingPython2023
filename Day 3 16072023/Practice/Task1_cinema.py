screening_type = input()
rows = int(input())
columns = int(input())
income = 0

cin_capacity = rows * columns

if screening_type == "Premiere":
    income = cin_capacity * 12.00
elif screening_type == "Normal":
    income = cin_capacity * 7.50
elif screening_type == "Discount":
    income = cin_capacity * 5.00

print(f"{income:.2f} leva")