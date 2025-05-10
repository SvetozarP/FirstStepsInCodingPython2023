area_greening=float(input())
price_for_greening=area_greening * 7.61
discount_total=price_for_greening * 0.18
total_final_price=price_for_greening - discount_total
print(f'The final price is: {total_final_price} lv.')
print(f'The discount is: {discount_total} lv.')