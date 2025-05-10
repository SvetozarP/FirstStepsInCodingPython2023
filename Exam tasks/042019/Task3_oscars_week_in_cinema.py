movie_name: str = input()
type_room: str = input()
ticket_number: int = int(input())
movie_price: float = 0
total_price: float = 0

if type_room == "normal":

    if movie_name == "A Star Is Born":
        movie_price = 7.5
    elif movie_name == "Bohemian Rhapsody":
        movie_price = 7.35
    elif movie_name == "Green Book":
        movie_price = 8.15
    elif movie_name == "The Favourite":
        movie_price = 8.75

elif type_room == "luxury":

    if movie_name == "A Star Is Born":
        movie_price = 10.5
    elif movie_name == "Bohemian Rhapsody":
        movie_price = 9.45
    elif movie_name == "Green Book":
        movie_price = 10.25
    elif movie_name == "The Favourite":
        movie_price = 11.55

elif type_room == "ultra luxury":

    if movie_name == "A Star Is Born":
        movie_price = 13.5
    elif movie_name == "Bohemian Rhapsody":
        movie_price = 12.75
    elif movie_name == "Green Book":
        movie_price = 13.25
    elif movie_name == "The Favourite":
        movie_price = 13.95

total_price = ticket_number * movie_price
print(f"{movie_name} -> {total_price:.2f} lv.")
