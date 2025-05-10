from math import pi

r_radius: float = float(input())

area = pi * r_radius * r_radius
perimeter = 2 * pi * r_radius

print(f"{area:.2f}")
print(f"{perimeter:.2f}")
