from sys import maxsize
init_number = int(input())
maxnum = -maxsize
sum_numbers = 0

for i in range (0, init_number):
    user_number = int(input())
    sum_numbers += user_number
    if user_number > maxnum:
        maxnum = user_number

if maxnum == sum_numbers - maxnum:
    print("Yes")
    print(f"Sum = {maxnum}")
else:
    diff = abs(sum_numbers - maxnum*2)
    print("No")
    print(f"Diff = {diff}")
