import pandas as pd
import plotly.express as px

# Read stock data from CSV file
stock_data = pd.read_csv("stock_data.csv")

# Convert 'Date' column to datetime
stock_data['Date'] = pd.to_datetime(stock_data['Date'])

# Create interactive line plot of stock closing prices over time
fig = px.line(stock_data, x='Date', y='Close', title='Interactive Stock Closing Prices over Time')

# Add hover information
fig.update_traces(hoverinfo='x+y', mode='lines+markers')

# Add range slider for date selection
fig.update_layout(xaxis=dict(rangeslider=dict(visible=True), type="date"))

# Add titles and labels
fig.update_layout(title="Interactive Stock Closing Prices over Time",
                  xaxis_title="Date",
                  yaxis_title="Closing Price")

# Show the interactive plot
fig.show()
