i_numbers = int(input())
sum_even = 0
sum_odd = 0

for i in range(0, i_numbers):
    n_number = int(input())
    if i % 2 == 0:
        sum_even += n_number
    elif i % 2 != 0:
        sum_odd += n_number

if sum_even == sum_odd:
    print("Yes")
    print(f"Sum = {sum_even}")
else:
    difference = abs(sum_even - sum_odd)
    print("No")
    print(f"Diff = {difference}")
