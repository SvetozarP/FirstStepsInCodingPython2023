from math import pi

fig_type = input()

if fig_type == "square":
    side_length = float(input())
    area_result = side_length * side_length

elif fig_type == "rectangle":
    side1_length = float(input())
    side2_length = float(input())
    area_result = side1_length * side2_length

elif fig_type == "circle":
    rad_length = float(input())
    area_result = pi * rad_length * rad_length

elif fig_type == "triangle":
    side_length = float(input())
    height_triangle = float(input())
    area_result = (side_length * height_triangle) / 2

else:
    print("Incorrect figure. Please choose square, rectangle, circle or triangle")
    area_result = 0

print(f"{area_result:.3f}")
