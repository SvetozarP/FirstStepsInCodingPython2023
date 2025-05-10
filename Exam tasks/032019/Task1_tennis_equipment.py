from math import floor
from math import ceil
racket_price: float = float(input())
count_rackets: int = int(input())
count_trainers: int = int(input())

price_trainers = racket_price / 6

total_rackets = racket_price * count_rackets
total_trainers = count_trainers * price_trainers
additional_eq = (total_rackets + total_trainers) * 0.2

total_price = total_rackets + total_trainers + additional_eq

sponsors_pay = ceil(total_price * 7 / 8)
djokovich_pay = floor(total_price * 1 / 8)

print(f"Price to be paid by Djokovic {djokovich_pay}")
print(f"Price to be paid by sponsors {sponsors_pay}")
