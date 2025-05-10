qty_nylon = int(input())
qty_paint = int(input())
qty_solution = int(input())
qty_hours = int(input())
bag_price = 0.4

qty_nylon_extra = qty_nylon + 2
qty_paint_exrea = qty_paint * 1.1

price_nylon = qty_nylon_extra * 1.5
price_paint = qty_paint_exrea * 14.5
price_solution = qty_solution * 5

total_materials = price_nylon + price_paint + price_solution + bag_price

labour_hourly = total_materials * 0.3

labour_total = qty_hours * labour_hourly

total_cost = total_materials + labour_total

print(total_cost)