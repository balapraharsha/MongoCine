# 🎬 MongoCine – TMDB Movies Analysis with Python & MongoDB  

## 📌 Overview
**MongoCine** is an end-to-end **Data Science project** analyzing TMDB movie metadata using **Python** and **MongoDB**.  

The system highlights:  
- **Data ingestion & storage using MongoDB**  
- **Data cleaning & preprocessing** with Pandas (missing values, type conversions, genre handling)  
- **Multi-level analysis** (basic, aggregation, advanced)  
- **Summary report generation** with key insights  
- **visualization for exploratory insights**  

---

## 📂 Project Structure

```

MongoCine/
├── movies_raw.csv               # Raw, unprocessed dataset
├── movies_clean.csv             # Cleaned dataset after preprocessing
├── insert_data.py               # Inserts movies into MongoDB using PyMongo and saves raw CSV
├── data_cleaning.py             # Cleans and preprocesses raw data
├── basic_analysis.py            # Performs basic analysis on cleaned data
├── aggregation_analysis.py      # MongoDB aggregation queries for insights
├── advanced_analysis.py         # Advanced analytics (ratings by year, genre, top movies)
├── data_visualisation.py        # Creates charts and graphs from data
├── summary_report.py            # Generates summary report (movies_summary_report.txt)
└── README.md                    # Project overview

```


---

## 🗄️ Dataset Overview
The dataset includes metadata of TMDB movies such as:  

| Column         | Description |
|----------------|------------|
| title          | Movie title |
| genres         | List of genres for the movie |
| vote_average   | Average rating of the movie |
| vote_count     | Number of votes |
| popularity     | Popularity score |
| release_date   | Release date of the movie |
| other columns  | Additional metadata included in TMDB |

> Raw data is stored in `movies_raw.csv` and cleaned data in `movies_clean.csv`.  

---

## ⚙️ Data Processing & Cleaning
- **Handle missing values** in `title`, `vote_average`, `genres`  
- **Convert numeric columns** (`vote_average`, `vote_count`, `popularity`)  
- **Convert release_date** to datetime  
- Replace empty genres with the **mode genre**  
- Save cleaned data to `movies_clean.csv`  

---

## 💻 MongoDB & PyMongo Usage
This project emphasizes **practical MongoDB skills**:  
- **Data insertion**: `insert_data.py` uses **PyMongo** to insert movies into MongoDB  
- **Aggregation**: `aggregation_analysis.py` uses MongoDB pipelines to:  
  - Compute average ratings by genre  
  - Compute ratings by release year  
  - Find top voted movies  
- **Querying**: Pull results from MongoDB into **Pandas** for deeper analysis  
- Demonstrates **full CRUD workflow**: create (insert), read (query/aggregate), update (clean/normalize), delete (if needed)  

---

## 📊 Data Analysis
Scripts include:  

- **basic_analysis.py** → Descriptive statistics, basic summaries  
- **aggregation_analysis.py** → MongoDB aggregations using PyMongo  
- **advanced_analysis.py** → Advanced analytics (ratings distribution, trends)  
- **summary_report.py** → Generates `movies_summary_report.txt`  

---

## 🔍 Insights & Patterns
From the analysis, we can uncover:  
- **Top Genres**: Most frequent genres
- **Ratings & Popularity**: Highest/lowest rated movies, average popularity  
- **Vote Trends**: Most voted movies, vote distribution  
- **Release Trends**: Growth in movies over the years  

---

## ▶️ How to Run
1. Install Python (v3.9+) and MongoDB  
2. Run `insert_data.py` → Inserts data into MongoDB using **PyMongo** and saves raw CSV  
3. Run `data_cleaning.py` → Cleans raw data and generates `movies_clean.csv`  
4. Run analysis scripts:  
   - `basic_analysis.py`  
   - `aggregation_analysis.py` (MongoDB aggregation queries)  
   - `advanced_analysis.py`  
5. Run `summary_report.py` → Generates summary report `movies_summary_report.txt`  
6. Optionally, run `data_visualisation.py` → Creates charts and graphs  

---

## 🛠️ Tools Used
- **Python** (Pandas, Matplotlib, PyMongo)  
- **MongoDB** for storage and aggregation  
- **Jupyter Notebook / VS Code**  

---

## 👨‍💻 Developed By
**Bala Praharsha .M**  
📧 balapraharsha.m@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/balapraharsha) | [GitHub](https://github.com/balapraharsha)  

---

⭐ Star the repo if you found this project helpful!  
