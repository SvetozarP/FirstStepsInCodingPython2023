number_of_pens = int(input())
number_of_markers = int(input())
ltr_cleaning_agent = int(input())
discount_number = int(input())

discount_percent = discount_number / 100

total_price_pens = number_of_pens * 5.8
total_price_markers = number_of_markers * 7.2
total_price_cleaning = ltr_cleaning_agent * 1.2

total_whole_price = total_price_pens + total_price_markers + total_price_cleaning
discounted_price = total_whole_price - (total_whole_price * discount_percent)

print(discounted_price)