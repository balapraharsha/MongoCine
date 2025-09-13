import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("movies_clean.csv")
df["release_year"] = pd.to_datetime(df["release_date"]).dt.year
df_genres = df.explode("genres")

# Top Rated Movies
top_rated = df.sort_values("vote_average", ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x="vote_average", y="title", data=top_rated, palette="viridis")
plt.title("Top Rated Movies")
plt.xlabel("Vote Average")
plt.ylabel("Movie")
plt.tight_layout()
plt.show()

# Most Popular Movies
top_popular = df.sort_values("popularity", ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x="popularity", y="title", data=top_popular, palette="plasma")
plt.title("Top Most Popular Movies")
plt.xlabel("Popularity")
plt.ylabel("Movie")
plt.tight_layout()
plt.show()

# Movies Released Per Year
movies_per_year = df.groupby("release_year").size().reset_index(name="movie_count")
plt.figure(figsize=(12,6))
sns.lineplot(x="release_year", y="movie_count", data=movies_per_year, marker="o")
plt.title("Movies Released Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6,5))
sns.heatmap(df[["vote_average","vote_count","popularity"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
