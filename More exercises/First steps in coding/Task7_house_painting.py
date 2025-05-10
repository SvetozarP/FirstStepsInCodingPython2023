x_wall: float = float(input())
y_wall: float = float(input())
h_height: float = float(input())

front_wall_area: float = x_wall * x_wall
area_door: float = 1.2 * 2
side_wall_area: float = x_wall * y_wall
window_area: float = 1.5 * 1.5

area_walls: float = 2 * front_wall_area + 2 * side_wall_area - area_door - 2 * window_area

need_green_paint: float = area_walls / 3.4

area_roof_rectangle: float = x_wall * y_wall
area_roof_triangle: float = x_wall * h_height / 2

total_roof_area: float = 2 * area_roof_triangle + 2 * area_roof_rectangle

need_red_paint: float = total_roof_area / 4.3

print(f"{need_green_paint:.2f}")
print(f"{need_red_paint:.2f}")
