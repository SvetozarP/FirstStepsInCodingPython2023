peter_budg = float(input())
no_vcards = int(input())
no_proces = int(input())
no_memory = int(input())
discount = 0.15

cost_vcard = no_vcards * 250
cost_single_proc = cost_vcard * 0.35
cost_single_mem = cost_vcard * 0.1

cost_proc = no_proces * cost_single_proc
cost_memory = cost_single_mem * no_memory

total_cost = cost_vcard + cost_memory + cost_proc

if no_vcards > no_proces:
    total_cost = total_cost - total_cost * discount

if peter_budg >= total_cost:
    budg_left = peter_budg - total_cost
    print(f"You have {budg_left:.2f} leva left!")
else:
    budg_need = total_cost - peter_budg
    print(f"Not enough money! You need {budg_need:.2f} leva more!")
