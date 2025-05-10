u_number = int(input())
b_points = 0
b_points_adit = 0
final_number = 0

if u_number <= 100:
    b_points = 5

elif 100 < u_number <= 1000:
    b_points = u_number * 0.2

else:
    b_points = u_number * 0.1

if u_number % 2 == 0:
    b_points_adit = 1

elif u_number % 10 == 5:
    b_points_adit = 2

final_bonus = b_points + b_points_adit
final_number = u_number + final_bonus

print(final_bonus)
print(final_number)
