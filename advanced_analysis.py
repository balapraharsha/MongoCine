import pandas as pd

# Load data
df_movies = pd.read_csv("movies_clean.csv")

# Explode Genres
df_genres = df_movies.explode("genres")

# Highest-Rated Movie per Genre
top_movie_per_genre = df_genres.loc[df_genres.groupby("genres")["vote_average"].idxmax()]
print("Highest-Rated Movie per Genre:")
print(top_movie_per_genre[["genres", "title", "vote_average", "vote_count"]], "\n")

# Most Popular Genre per Year
df_movies["release_year"] = pd.to_datetime(df_movies["release_date"]).dt.year
year_genre = df_movies.explode("genres").groupby(["release_year", "genres"]).agg(
    avg_popularity=("popularity", "mean")
).reset_index()

most_popular_genre_per_year = year_genre.loc[year_genre.groupby("release_year")["avg_popularity"].idxmax()]
print("Most Popular Genre per Year:")
print(most_popular_genre_per_year, "\n")

# Top 5 Movies per Year with Votes > 15000
top_movies_year = df_movies[df_movies["vote_count"] > 15000].sort_values(["release_year", "vote_average"], ascending=[True, False])
top5_per_year = top_movies_year.groupby("release_year").head(5)
print("Top 5 Movies per Year with Vote Count > 15000:")
print(top5_per_year[["release_year", "title", "vote_average", "vote_count"]], "\n")
