import pandas as pd

# Load data
df_movies = pd.read_csv("movies_clean.csv")

# Basic Info
print("DataFrame Info:")
print(df_movies.info(), "\n")

print("First 5 Rows:")
print(df_movies.head(), "\n")

print("Basic Statistics:")
print(df_movies.describe(include='all'), "\n")

# Top rated movies
top_rated = df_movies.sort_values("vote_average", ascending=False).head(10)
print("Top 10 Rated Movies:")
print(top_rated[["title", "vote_average", "vote_count"]], "\n")

# Most popular movies
top_popular = df_movies.sort_values("popularity", ascending=False).head(10)
print("Top 10 Popular Movies:")
print(top_popular[["title", "popularity", "vote_average"]], "\n")

# Movies with high votes
high_votes = df_movies[df_movies["vote_count"] >= 15000].sort_values("vote_count", ascending=False)
print("Movies with High Vote Count:")
print(high_votes[["title", "vote_count", "vote_average"]], "\n")

# Correlation analysis
corr = df_movies[["vote_count", "vote_average", "popularity"]].corr()
print("Correlation between Vote Count, Vote Average, and Popularity:")
print(corr, "\n")
