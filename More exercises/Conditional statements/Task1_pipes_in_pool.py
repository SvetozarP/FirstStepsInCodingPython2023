volume_litres: int = int(input())
depit_p1: int = int(input())
debit_p2: int = int(input())
hours_absence: float = float(input())

pipe1_for_time: float = depit_p1 * hours_absence
pipe2_for_time: float = debit_p2 * hours_absence

total_full: float = pipe1_for_time + pipe2_for_time

if total_full <= volume_litres:
    print(f"The pool is {total_full / volume_litres * 100:.2f}% full. Pipe 1: {pipe1_for_time / total_full * 100:.2f}"
          f"%. Pipe 2: {pipe2_for_time / total_full * 100:.2f}%.")
elif volume_litres < total_full:
    print(f"For {hours_absence:.2f} hours the pool overflows with {total_full - volume_litres:.2f} liters.")
