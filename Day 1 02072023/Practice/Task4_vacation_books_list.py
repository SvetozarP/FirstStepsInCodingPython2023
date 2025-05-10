from math import floor

page_count = int(input())
page_per_hour = int(input())
number_of_days = int(input())

total_time_to_read = page_count / page_per_hour
time_needed_per_day = total_time_to_read / number_of_days

print(floor(time_needed_per_day))