desired_height: int = int(input())
now_height: int = desired_height - 30
count_unsuccessful: int = 0
total_count: int = 0

while True:

    jump_height: int = int(input())
    total_count += 1

    if now_height >= jump_height:

        count_unsuccessful += 1

    else:

        now_height += 5
        count_unsuccessful = 0

    if now_height > desired_height:
        print(f"Tihomir succeeded, he jumped over {desired_height}cm after {total_count} jumps.")
        break

    if count_unsuccessful == 3:
        print(f"Tihomir failed at {now_height}cm after {total_count} jumps.")
        break
