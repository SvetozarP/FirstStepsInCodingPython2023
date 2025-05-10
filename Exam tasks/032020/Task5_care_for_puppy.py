qty_feed_kg = int(input())
qty_feed_gr: int = qty_feed_kg * 1000
total_eaten: int = 0

while True:
    qty_eaten: str = input()

    if qty_eaten == "Adopted":
        if total_eaten > qty_feed_gr:
            print(f"Food is not enough. You need {abs(total_eaten - qty_feed_gr)} grams more.")
        else:
            print(f"Food is enough! Leftovers: {abs(total_eaten - qty_feed_gr)} grams.")
        break

    else:

        total_eaten += int(qty_eaten)
