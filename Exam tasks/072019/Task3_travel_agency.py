name_town: str = input()
packet_type: str = input()
vip_discount: str = input()
days_stay: int = int(input())
price: float = 0
total_price: float = 0

if days_stay < 1:
    print("Days must be positive number!")

elif name_town != "Bansko" and name_town != "Borovets" and name_town != "Varna" and name_town != "Burgas":

    print("Invalid input!")

elif (name_town == "Bansko" or name_town == "Borovets") and \
        (packet_type != "noEquipment" and packet_type != "withEquipment"):

    print("Invalid input!")

elif (name_town == "Varna" or name_town == "Burgas") and \
        (packet_type != "noBreakfast" and packet_type != "withBreakfast"):

    print("Invalid input!")

else:
    if name_town == "Bansko" or name_town == "Borovets":
        if packet_type == "withEquipment":

            if vip_discount == "no":
                price = 100.00
            elif vip_discount == "yes":
                price = 100.00 * 0.9

        elif packet_type == "noEquipment":

            if vip_discount == "no":
                price = 80.00
            elif vip_discount == "yes":
                price = 80.00 * 0.95

    elif name_town == "Varna" or name_town == "Burgas":

        if packet_type == "withBreakfast":

            if vip_discount == "no":
                price = 130.00
            elif vip_discount == "yes":
                price = 130.00 * 0.88

        elif packet_type == "noBreakfast":

            if vip_discount == "no":
                price = 100.00
            elif vip_discount == "yes":
                price = 100.00 * 0.93

    if days_stay > 7:
        days_stay -= 1

    total_price = days_stay * price

    print(f"The price is {total_price:.2f}lv! Have a nice time!")
