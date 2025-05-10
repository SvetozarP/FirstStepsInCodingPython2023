from sys import maxsize
u_number = input()
smallest = maxsize

while u_number != "Stop":
    number = int(u_number)
    if number < smallest:
        smallest = number
    u_number = input()

print(smallest)