from sys import maxsize

number_movies: int = int(input())
max_rating = -maxsize
min_rating = maxsize
total_rating: float = 0.00
max_rate_movie: str = ""
min_rate_movie: str = ""

for _ in range(1, number_movies + 1):
    movie_name: str = input()
    movie_rate: float = float(input())

    if movie_rate < min_rating:
        min_rating = movie_rate
        min_rate_movie = movie_name

    if movie_rate > max_rating:
        max_rating = movie_rate
        max_rate_movie = movie_name

    total_rating += movie_rate

avg_rate = total_rating / number_movies

print(f"{max_rate_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_rate_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {avg_rate:.1f}")
