name_company: str = input()
count_senior_tick: int = int(input())
count_kids_tick: int = int(input())
price_senior: float = float(input())
tax_service: float = float(input())

price_kid: float = price_senior * 0.3
total_cost: float = count_senior_tick * (price_senior + tax_service) + count_kids_tick * (price_kid + tax_service)

profit: float = total_cost * 0.2

print(f"The profit of your agency from {name_company} tickets is {profit:.2f} lv.")
