bitcoin_count: int = int(input())
yuan_count: float = float(input())
change_commission: float = float(input())

bitcoin_cost_leva: int = bitcoin_count * 1168
yuan_to_dolar = yuan_count * 0.15
dolar_price: float = 1.76
yuan_cost_leva: float = yuan_to_dolar * dolar_price

euro_conversion: float = (bitcoin_cost_leva + yuan_cost_leva) / 1.95

comission: float = (euro_conversion) * change_commission / 100

total_evro: float = euro_conversion - comission

print(f"{total_evro:.2f}")
