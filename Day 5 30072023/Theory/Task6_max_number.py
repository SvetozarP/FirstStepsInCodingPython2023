from sys import maxsize
u_number = input()
biggest = -maxsize

while u_number != "Stop":
    number = int(u_number)
    if number > biggest:
        biggest = number
    u_number = input()

print(biggest)
