banknote_onelv: int = int(input())
banknote_twolv: int = int(input())
banknote_fivelv: int = int(input())
sum_to_pay: int = int(input())

for onelv in range(0, banknote_onelv + 1):
    for twolv in range(0, banknote_twolv + 1):
        for fivelv in range(0, banknote_fivelv + 1):

            if onelv * 1 + twolv * 2 + fivelv * 5 == sum_to_pay:

                print(f"{onelv} * 1 lv. + {twolv} * 2 lv. + {fivelv} * 5 lv. = {sum_to_pay} lv.")
