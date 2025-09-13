import pandas as pd
from pymongo import MongoClient

# Connect database
# Replace <MONGO_URI> with your MongoDB connection string
client = MongoClient("<MONGO_URI>") 
db = client['movies_db']
collection = db['movies']

df = pd.DataFrame(list(collection.find()))
print("Raw DataFrame shape:", df.shape)

# Drop MongoDB _id column if exists
if "_id" in df.columns:
    df = df.drop(columns=["_id"])

# Ensure all expected columns exist
expected_cols = ["title", "genres", "vote_average", "vote_count", "popularity", "release_date"]
for col in expected_cols:
    if col not in df.columns:
        # Add column with default values
        if col == "genres":
            df[col] = [["Unknown"]] * len(df)
        elif col in ["vote_average", "popularity"]:
            df[col] = 0.0
        elif col == "vote_count":
            df[col] = 0
        else:
            df[col] = None

# Handle Missing Values
# Drop rows with missing 'title' or 'vote_average'
df = df.dropna(subset=["title", "vote_average"])

# Fill missing or empty 'genres' with ["Unknown"]
df["genres"] = df["genres"].apply(lambda x: x if isinstance(x, list) and any(x) else [pd.Series([g for sublist in df["genres"] if isinstance(sublist, list) for g in sublist]).mode()[0]] )

# Convert Data Types
df["vote_average"] = pd.to_numeric(df["vote_average"], errors='coerce')
df["vote_count"] = pd.to_numeric(df["vote_count"], errors='coerce')
df["popularity"] = pd.to_numeric(df["popularity"], errors='coerce')
df["release_date"] = pd.to_datetime(df["release_date"], errors='coerce')

# Drop Rows with Remaining Missing Values
df = df.dropna()

# Reset Index
df = df.reset_index(drop=True)

# Save Cleaned Data
df.to_csv("movies_clean.csv", index=False)
print("Data preprocessed and saved to 'movies_clean.csv' successfully!")
print("Cleaned DataFrame shape:", df.shape)
