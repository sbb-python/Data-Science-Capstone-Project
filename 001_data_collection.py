import pandas as pd

# Define the URL for fetching stock data
url = "https://query1.finance.yahoo.com/v7/finance/download/SDPI?period1=1514764800&period2=1714764800&interval=1d&events=history"

# Read stock data from Yahoo Finance
stock_data = pd.read_csv(url)

# Display the first few rows of the data
print(stock_data.head())

# Save the data to a CSV file
stock_data.to_csv("stock_data.csv", index=False)
