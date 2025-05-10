days_feed: int = int(input())
total_qty_feed: float = float(input())
treats_qty: float = 0.00
dog_tally: int = 0
cat_tally: int = 0
treats_tally: float = 0.00

for day in range(1, days_feed + 1):
    dog_feed: int = int(input())
    dog_tally += dog_feed
    cat_feed: int = int(input())
    cat_tally += cat_feed
    treats_qty = 0.00

    if day % 3 == 0:
        treats_qty = (dog_feed + cat_feed) * 0.1
        treats_tally += treats_qty

print(f"Total eaten biscuits: {round(treats_tally)}gr.")
print(f"{(dog_tally + cat_tally)/total_qty_feed * 100:.2f}% of the food has been eaten.")
print(f"{dog_tally / (dog_tally + cat_tally) * 100:.2f}% eaten from the dog.")
print(f"{cat_tally / (dog_tally + cat_tally) * 100:.2f}% eaten from the cat.")
