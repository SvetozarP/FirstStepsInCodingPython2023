u_number = int(input())
combinations_count = 0

for x1 in range(0, u_number + 1):
    for x2 in range(0, u_number +1):
        for x3 in range(0, u_number+1):
            if x1 + x2 + x3 == u_number:
                combinations_count += 1

print(combinations_count)
