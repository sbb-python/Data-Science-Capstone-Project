import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Add this line to import seaborn

# Read stock data from CSV file
stock_data = pd.read_csv("stock_data.csv")

# Convert 'Date' column to datetime
stock_data['Date'] = pd.to_datetime(stock_data['Date'])

# Summary statistics
print(stock_data.describe())

# Time series analysis
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Date'], stock_data['Close'])
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Stock Closing Prices over Time')
plt.show()

# Correlation matrix
correlation_matrix = stock_data.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")  # Fix 'sns' reference
plt.title('Correlation Matrix')
plt.show()

# Histogram of stock prices
plt.figure(figsize=(8, 6))
plt.hist(stock_data['Close'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Closing Price')
plt.ylabel('Frequency')
plt.title('Histogram of Stock Closing Prices')
plt.show()
