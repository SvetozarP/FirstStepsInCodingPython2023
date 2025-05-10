number = int(input())
totnum = number * 2
sum_left = 0
sum_right = 0

for i in range(0, totnum):
    number_from_user = int(input())
    if i < number:
        sum_left += number_from_user
    else:
        sum_right += number_from_user

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    difference = abs(sum_left - sum_right)
    print(f"No, diff = {difference}")
