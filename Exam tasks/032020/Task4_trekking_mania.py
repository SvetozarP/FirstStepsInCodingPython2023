num_group = int(input())
total_climbers = 0
n_musala = 0
n_monblan = 0
n_kilimanjaro = 0
n_k2 = 0
n_everest = 0

for i in range(1, num_group+1):
    count_in_group = int(input())
    total_climbers += count_in_group
    if count_in_group <= 5:
        n_musala += count_in_group
    elif count_in_group <= 12:
        n_monblan += count_in_group
    elif count_in_group <= 25:
        n_kilimanjaro += count_in_group
    elif count_in_group <= 40:
        n_k2 += count_in_group
    elif count_in_group > 40:
        n_everest += count_in_group

print(f"{n_musala / total_climbers * 100:.2f}%")
print(f"{n_monblan / total_climbers * 100:.2f}%")
print(f"{n_kilimanjaro / total_climbers * 100:.2f}%")
print(f"{n_k2 / total_climbers * 100:.2f}%")
print(f"{n_everest / total_climbers * 100:.2f}%")
