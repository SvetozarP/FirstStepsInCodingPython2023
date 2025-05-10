deposit_sum = float(input())
deposit_term = int(input())
deposit_annual_index = float(input())

convert_annual_index_in_perc = deposit_annual_index / 100

total_sum = deposit_sum + deposit_term * ((deposit_sum * convert_annual_index_in_perc) / 12 )

print(total_sum)