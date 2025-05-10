qty_chicken_menu = int(input())
qty_fish_menu = int(input())
qty_vegetarian_menu = int(input())
delivery_price = 2.5

price_chicken_menu = qty_chicken_menu * 10.35
price_fish_menu = qty_fish_menu *  12.4
price_vegetarian_menu = qty_vegetarian_menu * 8.15

total_menu_price = price_chicken_menu + price_fish_menu + price_vegetarian_menu

desert_price = total_menu_price * 0.2

total_order_price = total_menu_price + delivery_price + desert_price

print(total_order_price)