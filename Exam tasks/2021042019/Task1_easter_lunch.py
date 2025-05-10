number_kozunak: int = int(input())
number_eggs_pack: int = int(input())
kg_cookies: int = int(input())

cost_kozunak = 3.2 * number_kozunak
cost_eggs_pack = 4.35 * number_eggs_pack
cost_paint_egg = number_eggs_pack * 12 * 0.15
cost_cookie = 5.4 * kg_cookies

total_cost: float = cost_kozunak + cost_paint_egg + cost_eggs_pack + cost_cookie

print(f"{total_cost:.2f}")
