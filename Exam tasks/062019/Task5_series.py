budget_series: float = float(input())
number_series: int = int(input())
total_spend: float = 0.00

for _ in range(1, number_series + 1):
    name_series: str = input()
    series_price: float = float(input())

    if name_series == "Thrones":
        series_price = series_price * 0.5
    elif name_series == "Lucifer":
        series_price = series_price * 0.6
    elif name_series == "Protector":
        series_price = series_price * 0.7
    elif name_series == "TotalDrama":
        series_price = series_price * 0.8
    elif name_series == "Area":
        series_price = series_price * 0.9

    total_spend += series_price

diff = abs(total_spend - budget_series)

if budget_series >= total_spend:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")
