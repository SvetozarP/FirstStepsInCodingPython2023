u_speed = float(input())

if u_speed <= 10:
    print("slow")

elif 10 < u_speed <= 50:
    print("average")

elif 50 < u_speed <= 150:
    print("fast")

elif 150 < u_speed <= 1000:
    print("ultra fast")

else:
    print("extremely fast")
