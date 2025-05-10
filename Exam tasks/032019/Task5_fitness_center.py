number_attendees: int = int(input())
train_back: int = 0
train_chest: int = 0
train_leg: int = 0
train_abs: int = 0
buy_protein_shake: int = 0
buy_protein_bar: int = 0
total_train: int = 0
total_protein: int = 0

for _ in range(1, number_attendees + 1):

    activity = input()

    if activity == "Back":
        train_back += 1
    elif activity == "Chest":
        train_chest += 1
    elif activity == "Legs":
        train_leg += 1
    elif activity == "Abs":
        train_abs += 1
    elif activity == "Protein shake":
        buy_protein_shake += 1
    elif activity == "Protein bar":
        buy_protein_bar += 1

total_train = train_back + train_abs + train_leg + train_chest
total_protein = buy_protein_bar + buy_protein_shake

print(f"{train_back} - back")
print(f"{train_chest} - chest")
print(f"{train_leg} - legs")
print(f"{train_abs} - abs")
print(f"{buy_protein_shake} - protein shake")
print(f"{buy_protein_bar} - protein bar")
print(f"{total_train / number_attendees * 100:.2f}% - work out")
print(f"{total_protein / number_attendees * 100:.2f}% - protein")
