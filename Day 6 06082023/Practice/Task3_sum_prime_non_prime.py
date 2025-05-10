input_number = input()
sum_prime = 0
sum_nprime = 0
isprime = True
calculate = True

while input_number != "stop":

    if int(input_number) < 0:
        print("Number is negative.")
        calculate = False

    elif 0 >= int(input_number) == 1:
        sum_nprime += int(input_number)

    elif int(input_number) > 1:

        for i in range(2, int(input_number)):

            if (int(input_number) % i) == 0:
                isprime = False
                break
    if isprime and calculate:
        sum_prime += int(input_number)
    elif not isprime and calculate:
        sum_nprime += int(input_number)

    calculate = True
    isprime = True
    input_number = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_nprime}")
