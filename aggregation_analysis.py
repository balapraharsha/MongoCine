from pymongo import MongoClient
import pandas as pd

# Connect Database
# Replace <MONGO_URI> with your MongoDB connection string
client = MongoClient("<MONGO_URI>") 
db = client['movies_db']
collection = db['movies']

# Average Ratings by Genre
pipeline_genre = [
    {"$unwind": "$genres"},  # explode genres array
    {"$group": {
        "_id": "$genres",
        "avg_rating": {"$avg": {"$toDouble": "$vote_average"}},
        "total_votes": {"$sum": {"$toInt": "$vote_count"}},
        "movie_count": {"$sum": 1}
    }},
    {"$sort": {"avg_rating": -1}}
]

results_genre = list(collection.aggregate(pipeline_genre))
df_genre = pd.DataFrame(results_genre).rename(columns={"_id": "genre"})
print("\nAverage Ratings by Genre:")
print(df_genre)

# Average Ratings by Year
pipeline_year = [
    {"$addFields": {"release_year": {"$year": {"$toDate": "$release_date"}}}},
    {"$group": {
        "_id": "$release_year",
        "avg_rating": {"$avg": {"$toDouble": "$vote_average"}},
        "total_votes": {"$sum": {"$toInt": "$vote_count"}},
        "movie_count": {"$sum": 1}
    }},
    {"$sort": {"_id": 1}}
]

results_year = list(collection.aggregate(pipeline_year))
df_year = pd.DataFrame(results_year).rename(columns={"_id": "year"})
print("\nAverage Ratings by Year:")
print(df_year)

# Top 10 Movies by Vote Count
pipeline_top_votes = [
    {"$project": {
        "title": 1,
        "vote_average": {"$toDouble": "$vote_average"},
        "vote_count": {"$toInt": "$vote_count"},
        "popularity": 1
    }},
    {"$sort": {"vote_count": -1}},
    {"$limit": 10}
]

results_top_votes = list(collection.aggregate(pipeline_top_votes))
df_top_votes = pd.DataFrame(results_top_votes)
print("\nTop 10 Movies by Vote Count:")
print(df_top_votes[["title", "vote_average", "vote_count", "popularity"]])

# Summary of Insights
print("\nSummary:")
print(f"- Total genres analyzed: {df_genre.shape[0]}")
print(f"- Years covered: {df_year['year'].min()} to {df_year['year'].max()}")
print(f"- Top movie by votes: {df_top_votes.iloc[0]['title']} ({df_top_votes.iloc[0]['vote_count']} votes)")
