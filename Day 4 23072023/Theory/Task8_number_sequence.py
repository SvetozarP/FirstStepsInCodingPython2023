import sys
smallest = sys.maxsize
biggest = -sys.maxsize

count = int(input())

for n in range(0, count):
    num = int(input())

    if num < smallest:
        smallest = num

    if num > biggest:
        biggest = num

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")
