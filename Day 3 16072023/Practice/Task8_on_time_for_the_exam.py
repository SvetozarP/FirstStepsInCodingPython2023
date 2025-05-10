from math import floor

exam_h = int(input())
exam_m = int(input())
arrive_h = int(input())
arrive_m = int(input())

exam_h_to_m = exam_h * 60
arrive_h_to_m = arrive_h * 60

tot_exam_h_to_m = exam_h_to_m + exam_m
tot_arrive_h_to_m = arrive_h_to_m + arrive_m
arrive_on_time = tot_arrive_h_to_m - tot_exam_h_to_m

if arrive_on_time == 0:
    print("On time")

elif -30 <= arrive_on_time <0:
    print("On time")
    conv_arrive_m = abs(arrive_on_time) % 60
    print(f"{conv_arrive_m} minutes before the start")

elif arrive_on_time < -30:
    conv_arrive_h = abs(arrive_on_time) / 60
    conv_arrive_h = floor(conv_arrive_h)
    conv_arrive_m = abs(arrive_on_time) % 60
    if conv_arrive_h < 1:
        print("Early")
        print(f"{conv_arrive_m} minutes before the start")
    elif conv_arrive_h >= 1:
        print("Early")
        if conv_arrive_m < 10:
            print(f"{conv_arrive_h}:0{conv_arrive_m} hours before the start")
        else:
            print(f"{conv_arrive_h}:{conv_arrive_m} hours before the start")

elif arrive_on_time > 0:
    conv_arrive_h = arrive_on_time / 60
    conv_arrive_h = floor(conv_arrive_h)
    conv_arrive_m = arrive_on_time % 60
    if conv_arrive_h < 1:
        print("Late")
        print(f"{conv_arrive_m} minutes after the start")
    elif conv_arrive_h >= 1:
        print("Late")
        if conv_arrive_m < 10:
            print(f"{conv_arrive_h}:0{conv_arrive_m} hours after the start")
        else:
            print(f"{conv_arrive_h}:{conv_arrive_m} hours after the start")
