n = int(input())

print(f"{'*' * 2 * n}{' ' * n}{'*' * 2 * n}")

for row in range(n - 2):
    if row == int((n-1) / 2 - 1):
        print(f"*{'/' * 2 * (n - 1)}*{'|' * n}*{'/' * 2 * (n - 1)}*")
    else:
        print(f"*{'/' * 2 * (n - 1)}*{' ' * n}*{'/' * 2 * (n - 1)}*")

print(f"{'*' * 2 * n}{' ' * n}{'*' * 2 * n}")
