tank_length = int(input())
tank_width = int(input())
tank_heigth = int(input())
pc_taken = float(input())

pc_taken_to_pc = pc_taken / 100

tank_volume = tank_heigth * tank_width * tank_length

tank_vol_to_ltr = tank_volume / 1000

ltrs_needed = tank_vol_to_ltr * (1 - pc_taken_to_pc)

print(ltrs_needed)