rent_price = int(input())

price_statue = rent_price * 0.7
catering_price = price_statue * 0.85
sound_price = catering_price / 2

total_price = rent_price + price_statue + catering_price + sound_price


print(f"{total_price:.2f}")