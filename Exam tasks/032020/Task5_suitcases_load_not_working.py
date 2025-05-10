total_capacity: float = float(input())
volume_taken: float = 0.0
suitcase_no: int = 0
additional_volume: float = 0.0

while True:

    volume_suitcase: str = input()
    additional_volume = 0.0

    if volume_suitcase == "End":
        print(f"Congratulations! All suitcases are loaded!")
        break

    else:

        suitcase_no += 1

        if suitcase_no % 3 == 0 and suitcase_no >= 3:
            additional_volume = float(volume_suitcase) * 0.1
            volume_taken += float(volume_suitcase) + round(additional_volume, 2)
        else:
            volume_taken += float(volume_suitcase)

        if volume_taken >= total_capacity:
            print(f"No more space!")
            if volume_taken > total_capacity:
                suitcase_no -= 1
            break

print(f"Statistic: {suitcase_no} suitcases loaded.")
