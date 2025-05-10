init_numbers = int(input())
p1_numbers = 0
p2_numbers = 0
p3_numbers = 0
p4_numbers = 0
p5_numbers = 0

for i in range(0,init_numbers):
    u_number = int(input())

    if u_number < 200:
        p1_numbers += 1
    elif 200 <= u_number < 400:
        p2_numbers += 1
    elif 400 <= u_number < 600:
        p3_numbers += 1
    elif 600 <= u_number < 800:
        p4_numbers += 1
    elif 800 <= u_number <= 1000:
        p5_numbers += 1

print(f"{p1_numbers / init_numbers * 100:.2f}%")
print(f"{p2_numbers / init_numbers * 100:.2f}%")
print(f"{p3_numbers / init_numbers * 100:.2f}%")
print(f"{p4_numbers / init_numbers * 100:.2f}%")
print(f"{p5_numbers / init_numbers * 100:.2f}%")
