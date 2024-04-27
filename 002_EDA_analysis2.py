import pandas as pd
import numpy as np
from scipy.stats import mstats

# Step 1: Load Data
df = pd.read_csv("stock_data.csv")

# Check column names and first few rows of the DataFrame
print("Column Names:")
print(df.columns)
print("\nFirst Few Rows:")
print(df.head())

# Step 2: Explore Data
print("\nData Information:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Step 3: Handle Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Handle Duplicates
print("\nNumber of Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()

# Step 5: Convert Data Types
# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Step 6: Transform Data
# Calculate daily returns
df['Daily_Return'] = df['Close'].pct_change()

# Step 7: Handle Outliers
# Winsorize outliers in 'Daily_Return' column
df['Daily_Return'] = mstats.winsorize(df['Daily_Return'], limits=[0.05, 0.05])

# Step 8: Handle Inconsistencies
# No inconsistencies identified in this example

# Step 9: Export Data
df.to_csv("cleaned_stock_data.csv", index=False)

# Step 10: Export Cleaned Data
print("\nCleaned Data Saved Successfully!")
