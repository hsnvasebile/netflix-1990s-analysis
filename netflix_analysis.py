import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("netflix_data.csv")

movies = netflix_df[netflix_df["type"] == "Movie"]

movies_1990s = movies[
    (movies["release_year"] >= 1990) &
    (movies["release_year"] < 2000)
]

duration = int(movies_1990s["duration"].mode()[0])

short_action_movies = movies_1990s[
    (movies_1990s["genre"] == "Action") &
    (movies_1990s["duration"] < 90)
]

short_movie_count = len(short_action_movies)

print(duration)
print(short_movie_count)
