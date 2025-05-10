from sys import maxsize

numbers_to_read: int = int(input())

oddsum: float = 0.0
oddmin: float = maxsize
oddmax: float = -maxsize
evensum: float = 0.0
evenmin: float = maxsize
evenmax: float = -maxsize

for number in range(1, numbers_to_read + 1):

    usernum: float = float(input())

    if number % 2:

        oddsum += usernum

        if usernum > oddmax:
            oddmax = usernum

        if usernum < oddmin:
            oddmin = usernum

    elif not number % 2:

        evensum += usernum

        if usernum > evenmax:
            evenmax = usernum

        if usernum < evenmin:
            evenmin = usernum

if oddsum == 0.0:
    print(f"OddSum={oddsum:.2f},")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
elif oddsum != 0.0:
    print(f"OddSum={oddsum:.2f},")
    print(f"OddMin={oddmin:.2f},")
    print(f"OddMax={oddmax:.2f},")

if evensum == 0.0:
    print(f"EvenSum={evensum:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
elif evensum != 0.0:
    print(f"EvenSum={evensum:.2f},")
    print(f"EvenMin={evenmin:.2f},")
    print(f"EvenMax={evenmax:.2f}")
