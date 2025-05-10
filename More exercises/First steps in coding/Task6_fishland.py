price_skumria_kg: float = float(input())
price_caca_kg: float = float(input())
kg_palamud: float = float(input())
kg_safrid: float = float(input())
kg_midi: int = int(input())

price_palamud: float = price_skumria_kg * 1.6
price_safrid: float = price_caca_kg * 1.8
price_midi: float = 7.5

cost_palamud: float = kg_palamud * price_palamud
cost_safrid: float = kg_safrid * price_safrid
cost_midi = kg_midi * price_midi

total_cost = cost_palamud + cost_safrid + cost_midi

print(f"{total_cost:.2f}")
