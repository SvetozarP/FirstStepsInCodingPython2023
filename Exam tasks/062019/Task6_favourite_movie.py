from sys import maxsize

movie_name: str = input()
count_movies: int = 0
max_rating: float = -maxsize
movie_rating: float = 0
win_name: str = ""
limit_reached: bool = False

while True:

    count_movies += 1
    movie_rating = 0

    if movie_name == "STOP":
        break
    elif count_movies == 7:
        limit_reached = True
        break
    else:

        name_length: int = len(movie_name)

        for character in movie_name:

            movie_rating += ord(character)

            if character.isupper():
                movie_rating -= name_length
            elif character.islower():
                movie_rating -= name_length * 2

        if movie_rating > max_rating:
            win_name = movie_name
            max_rating = movie_rating

    movie_name = input()

if limit_reached:
    print("The limit is reached.")

print(f"The best movie for you is {win_name} with {max_rating} ASCII sum.")
