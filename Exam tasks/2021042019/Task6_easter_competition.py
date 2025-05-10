from sys import maxsize

number_kozunak: int = int(input())
total_assessment: int = 0
max_assessment: int = -maxsize
baker_no_one: str = ""

for _ in range(1, number_kozunak + 1):

    baker_name: str = input()

    while True:

        kozunak_assessment: str = input()

        if kozunak_assessment == "Stop":

            break

        else:
            total_assessment += int(kozunak_assessment)

    print(f"{baker_name} has {total_assessment} points.")

    if total_assessment > max_assessment:
        max_assessment = total_assessment
        baker_no_one = baker_name

        print(f"{baker_name} is the new number 1!")

    total_assessment = 0

print(f"{baker_no_one} won competition with {max_assessment} points!")
