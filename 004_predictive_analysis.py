import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Load and Prepare Data
stock_data = pd.read_csv("stock_data.csv")

# Select relevant features and target variable
X = stock_data[['Open', 'High', 'Low', 'Volume']]  # Features
y = stock_data['Close']  # Target variable

# Step 2: Split Data into Train and Test Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the Model
model = LinearRegression()  # Initialize linear regression model
model.fit(X_train, y_train)  # Train the model using the training data

# Step 4: Make Predictions
predictions = model.predict(X_test)  # Use the trained model to make predictions on the test data

# Step 5: Evaluate the Model
mse = mean_squared_error(y_test, predictions)  # Calculate Mean Squared Error (MSE)
print("Mean Squared Error:", mse)
