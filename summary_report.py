import pandas as pd

# Load cleaned CSV
df = pd.read_csv("movies_clean.csv")

# General Information
total_movies = df.shape[0]
total_genres = len(set([g for sublist in df["genres"].apply(eval) for g in sublist]))
date_range = (df["release_date"].min(), df["release_date"].max())

# Ratings Summary
avg_rating = df["vote_average"].mean()
max_rating = df["vote_average"].max()
min_rating = df["vote_average"].min()

# Popularity & Votes
avg_popularity = df["popularity"].mean()
max_votes = df["vote_count"].max()
top_movie_votes = df.loc[df["vote_count"].idxmax(), "title"]

# Top Genres by Movie Count
all_genres = [g for sublist in df["genres"].apply(eval) for g in sublist if g != "Unknown"]
mode_series = pd.Series(all_genres).mode()
top_genre = mode_series[0] if not mode_series.empty else "No Genre"

# Summary Report Output
report = f"""
===================== MOVIES DATA SUMMARY =====================

Total Movies: {total_movies}
Unique Genres: {total_genres}
Release Date Range: {date_range[0]} to {date_range[1]}

Ratings:
- Average Rating: {avg_rating:.2f}
- Highest Rating: {max_rating}
- Lowest Rating: {min_rating}

Popularity & Votes:
- Average Popularity: {avg_popularity:.2f}
- Most Voted Movie: {top_movie_votes} ({max_votes} votes)

Top Genre: {top_genre}

===============================================================
"""

# Print report
print(report)

# Save report to text file
with open("movies_summary_report.txt", "w") as f:
    f.write(report)
print("Summary report saved to 'movies_summary_report.txt'")
