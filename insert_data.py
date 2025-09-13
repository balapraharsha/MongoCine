from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
# Replace <MONGO_URI> with your MongoDB connection string
client = MongoClient("<MONGO_URI>")  
db = client['movies_db']
collection = db['movies']

# Clear collection if already exists
collection.delete_many({})

# Sample data
movies_data = [
    {"title": "Inception", "genres": ["Action", "Sci-Fi"], "vote_average": "8.8", "vote_count": 21000, "popularity": 95.0, "release_date": "2010-07-16"},
    {"title": "The Dark Knight", "genres": ["Action", "Crime", "Drama"], "vote_average": 9.0, "vote_count": "23000", "popularity": 98.0, "release_date": "2008-07-18"},
    {"title": "Interstellar", "genres": ["Adventure", "Drama", "Sci-Fi"], "vote_average": 8.6, "vote_count": 17000, "popularity": 90.0, "release_date": "2014-11-07"},
    {"title": None, "genres": ["Thriller"], "vote_average": 7.5, "vote_count": 12000, "popularity": 85.0, "release_date": "2019-01-01"},  # missing title
    {"title": "Parasite", "genres": [], "vote_average": 8.5, "vote_count": 11000, "popularity": 85.0, "release_date": "2019-05-30"},  # empty genres
    {"title": "Avengers: Endgame", "genres": ["Action", "Adventure"], "vote_average": "8.4", "vote_count": "25000", "popularity": 120.0, "release_date": "2019-04-26"},
    {"title": "Titanic", "genres": ["Drama", "Romance"], "vote_average": 7.8, "vote_count": 20000, "popularity": 80.0, "release_date": "1997-12-19"},
    {"title": "Joker", "genres": ["Crime", "Drama", "Thriller"], "vote_average": "8.5", "vote_count": 19000, "popularity": 95.0, "release_date": "2019-10-04"},
    {"title": "The Godfather", "genres": ["Crime", "Drama"], "vote_average": 9.2, "vote_count": 16000, "popularity": 70.0, "release_date": "1972-03-24"},
    {"title": "Pulp Fiction", "genres": ["Crime", "Drama"], "vote_average": 8.9, "vote_count": 15000, "popularity": 65.0, "release_date": "1994-10-14"},
    {"title": "The Shawshank Redemption", "genres": ["Drama"], "vote_average": 9.3, "vote_count": 17000, "popularity": 60.0, "release_date": "1994-09-23"},
    {"title": "The Matrix", "genres": ["Action", "Sci-Fi"], "vote_average": 8.7, "vote_count": 14000, "popularity": 88.0, "release_date": "1999-03-31"},
    {"title": "Fight Club", "genres": ["Drama"], "vote_average": "8.8", "vote_count": 14500, "popularity": 70.0, "release_date": "1999-10-15"},
    {"title": "Forrest Gump", "genres": ["Drama", "Romance"], "vote_average": 8.8, "vote_count": 16000, "popularity": 75.0, "release_date": "1994-07-06"},
    {"title": "Gladiator", "genres": ["Action", "Adventure", "Drama"], "vote_average": 8.5, "vote_count": "14000", "popularity": 85.0, "release_date": "2000-05-05"},
    {"title": "Avengers: Infinity War", "genres": ["Action", "Adventure"], "vote_average": 8.4, "vote_count": 22000, "popularity": 115.0, "release_date": "2018-04-27"},
    {"title": "The Lion King", "genres": ["Animation", "Adventure", "Drama"], "vote_average": "8.5", "vote_count": 18000, "popularity": 90.0, "release_date": "1994-06-24"},
    {"title": "The Silence of the Lambs", "genres": ["Crime", "Drama", "Thriller"], "vote_average": 8.6, "vote_count": 13000, "popularity": 68.0, "release_date": "1991-02-14"},
    {"title": "Schindler's List", "genres": ["Biography", "Drama", "History"], "vote_average": 8.9, "vote_count": 11000, "popularity": 55.0, "release_date": "1993-12-15"},
    {"title": "Toy Story", "genres": ["Animation", "Adventure", "Comedy"], "vote_average": 8.3, "vote_count": 12500, "popularity": 80.0, "release_date": "1995-11-22"},
    {"title": "Coco", "genres": ["Animation", "Adventure", "Family"], "vote_average": 8.4, "vote_count": 10500, "popularity": 75.0, "release_date": "2017-11-22"},
    {"title": "Moana", "genres": ["Animation", "Adventure", "Comedy"], "vote_average": 7.6, "vote_count": 9500, "popularity": 70.0, "release_date": "2016-11-23"},
    {"title": "Frozen", "genres": ["Animation", "Adventure", "Comedy"], "vote_average": "7.4", "vote_count": 10000, "popularity": 85.0, "release_date": "2013-11-27"},
    {"title": "Black Panther", "genres": ["Action", "Adventure", "Sci-Fi"], "vote_average": 7.3, "vote_count": 15000, "popularity": 105.0, "release_date": "2018-02-16"},
    {"title": "Guardians of the Galaxy", "genres": ["Action", "Adventure", "Sci-Fi"], "vote_average": 8.0, "vote_count": 12000, "popularity": 95.0, "release_date": "2014-08-01"},
    {"title": "Deadpool", "genres": ["Action", "Comedy"], "vote_average": 8.0, "vote_count": 13500, "popularity": 98.0, "release_date": "2016-02-12"},
    {"title": "Logan", "genres": ["Action", "Drama"], "vote_average": 8.1, "vote_count": 11000, "popularity": 85.0, "release_date": "2017-03-03"},
    {"title": "Jumanji: Welcome to the Jungle", "genres": ["Action", "Adventure", "Comedy"], "vote_average": 6.9, "vote_count": 9500, "popularity": 80.0, "release_date": "2017-12-20"},
    {"title": "Wonder Woman", "genres": ["Action", "Adventure", "Fantasy"], "vote_average": 7.4, "vote_count": 10000, "popularity": 90.0, "release_date": "2017-06-02"},
    {"title": "Aquaman", "genres": ["Action", "Adventure", "Fantasy"], "vote_average": 6.9, "vote_count": 10500, "popularity": 88.0, "release_date": "2018-12-21"},
    {"title": "The Revenant", "genres": ["Action", "Adventure", "Drama"], "vote_average": 8.0, "vote_count": 9000, "popularity": 70.0, "release_date": "2015-12-25"},
    {"title": "Mad Max: Fury Road", "genres": ["Action", "Adventure", "Sci-Fi"], "vote_average": 8.1, "vote_count": 9500, "popularity": 92.0, "release_date": "2015-05-15"},
    {"title": "Star Wars: The Force Awakens", "genres": ["Action", "Adventure", "Sci-Fi"], "vote_average": 7.8, "vote_count": 20000, "popularity": 110.0, "release_date": "2015-12-18"},
    {"title": "Rogue One", "genres": ["Action", "Adventure", "Sci-Fi"], "vote_average": 7.8, "vote_count": 15000, "popularity": 100.0, "release_date": "2016-12-16"},
    {"title": "Solo: A Star Wars Story", "genres": ["Action", "Adventure", "Sci-Fi"], "vote_average": 6.9, "vote_count": 8000, "popularity": 70.0, "release_date": "2018-05-25"},
    {"title": "The Martian", "genres": ["Adventure", "Drama", "Sci-Fi"], "vote_average": 8.0, "vote_count": 13000, "popularity": 90.0, "release_date": "2015-10-02"},
    {"title": "Gravity", "genres": ["Drama", "Sci-Fi", "Thriller"], "vote_average": 7.7, "vote_count": 10000, "popularity": 80.0, "release_date": "2013-10-04"},
    {"title": "La La Land", "genres": ["Comedy", "Drama", "Music"], "vote_average": 8.0, "vote_count": 12000, "popularity": 85.0, "release_date": "2016-12-25"},
    {"title": "The Irishman", "genres": ["Biography", "Crime", "Drama"], "vote_average": 7.8, "vote_count": 9000, "popularity": 70.0, "release_date": "2019-11-01"},
    {"title": "Bird Box", "genres": ["Drama", "Horror", "Sci-Fi"], "vote_average": 6.6, "vote_count": 8000, "popularity": 75.0, "release_date": "2018-12-21"},
    {"title": "Roma", "genres": ["Drama"], "vote_average": 7.7, "vote_count": 6500, "popularity": 60.0, "release_date": "2018-08-30"},
    {"title": "The Social Network", "genres": ["Biography", "Drama"], "vote_average": 7.7, "vote_count": 9000, "popularity": 68.0, "release_date": "2010-10-01"},
    {"title": "Gone Girl", "genres": ["Drama", "Mystery", "Thriller"], "vote_average": 8.1, "vote_count": 11000, "popularity": 80.0, "release_date": "2014-10-03"},
    {"title": "The Big Short", "genres": ["Biography", "Comedy", "Drama"], "vote_average": 7.8, "vote_count": 9500, "popularity": 70.0, "release_date": "2015-12-11"},
    {"title": "Slumdog Millionaire", "genres": ["Drama", "Romance"], "vote_average": 8.0, "vote_count": 9000, "popularity": 65.0, "release_date": "2008-11-12"},
    {"title": "12 Years a Slave", "genres": ["Biography", "Drama", "History"], "vote_average": 8.1, "vote_count": 8500, "popularity": 60.0, "release_date": "2013-10-18"},
    {"title": "The Hateful Eight", "genres": ["Crime", "Drama", "Mystery"], "vote_average": 7.8, "vote_count": 7000, "popularity": 55.0, "release_date": "2015-12-30"},
    {"title": "Dunkirk", "genres": ["Action", "Drama", "History"], "vote_average": 7.9, "vote_count": 8000, "popularity": 65.0, "release_date": "2017-07-21"},
    {"title": "Bohemian Rhapsody", "genres": ["Biography", "Drama", "Music"], "vote_average": 7.9, "vote_count": 12000, "popularity": 85.0, "release_date": "2018-10-24"},
    {"title": "A Star Is Born", "genres": ["Drama", "Music", "Romance"], "vote_average": 7.6, "vote_count": 9500, "popularity": 70.0, "release_date": "2018-10-05"},
]

# Insert into MongoDB
collection.insert_many(movies_data)
print(f"{len(movies_data)} movies inserted successfully!")

# Save raw data to csv
df_raw = pd.DataFrame(movies_data)
df_raw.to_csv("movies_raw.csv", index=False)
print("Raw movies data saved as 'movies_raw.csv'")