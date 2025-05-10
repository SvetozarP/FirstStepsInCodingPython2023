movie_name = input()
no_days = int(input())
no_tickets = int(input())
price_per_ticket = float(input())
perc_cinema = int(input())

sales_price = no_days * no_tickets * price_per_ticket
for_cinema = sales_price * perc_cinema / 100

profit = sales_price - for_cinema

print(f"The profit from the movie {movie_name} is {profit:.2f} lv.")
