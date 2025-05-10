total_capacity: float = float(input())

counter: int = 0

while True:
    volume_suitcase: str = input()

    if volume_suitcase == 'End':
        print(f'Congratulations! All suitcases are loaded!\nStatistic: {counter} suitcases loaded.')
        break

    suitcase: float = float(volume_suitcase)
    if (counter + 1) % 3 == 0:
        suitcase *= 1.1

    if suitcase > total_capacity:
        print(f'No more space!\nStatistic: {counter} suitcases loaded.')
        break

    total_capacity -= suitcase
    counter += 1
