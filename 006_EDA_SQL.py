import pandas as pd
import sqlite3
import requests

# Step 1: Download data from Yahoo Finance URL
url = "https://query1.finance.yahoo.com/v7/finance/download/SDPI?period1=1514764800&period2=1714764800&interval=1d&events=history"
response = requests.get(url)
with open("SDPI.csv", "wb") as f:
    f.write(response.content)

# Step 2: Read CSV File into DataFrame
df = pd.read_csv("SDPI.csv")

# Step 3: Connect to SQLite Database and Write DataFrame to Table
conn = sqlite3.connect("stock_data.db")
df.to_sql("stock_prices", conn, index=False, if_exists="replace")

# Step 4: Perform EDA with SQL Queries
# Example: Calculate summary statistics
summary_query = """
    SELECT 
        MIN("Open") AS min_open, 
        MAX("High") AS max_high, 
        AVG("Close") AS avg_close 
    FROM 
        stock_prices;
"""
summary_stats = pd.read_sql_query(summary_query, conn)
print("Summary Statistics:")
print(summary_stats)

# Example: Data Exploration - Unique values and their counts for a column
unique_values_query = """
    SELECT 
        column_name, 
        COUNT(*) AS count 
    FROM 
        stock_prices 
    GROUP BY 
        column_name;
"""
unique_values = pd.read_sql_query(unique_values_query, conn)
print("Unique Values and Counts:")
print(unique_values)

# Step 5: Close Connection
conn.close()
