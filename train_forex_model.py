import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
df = pd.read_csv("forex_data.csv")

# Convert Date column to datetime (Handle errors)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Drop rows where Date conversion failed (if any)
df = df.dropna(subset=['Date'])

# Define features (X) and target variable (y)
X = df[['Open', 'High', 'Low', 'Volume']]  # Features
y = df['Close']  # Target variable

# Handle missing values in X
X = X.fillna(X.mean())  # Replace NaN in features with mean values

# Convert y to numeric and handle missing values
y = pd.to_numeric(y, errors='coerce')  # Convert non-numeric to NaN
y = y.fillna(y.mean())  # Replace NaN in target with mean value

# Check for any remaining NaN values (debugging)
print("Missing values in X:", X.isna().sum().sum())
print("Missing values in y:", y.isna().sum())

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)  # Fit the model

# Print model score
print("Model training completed. R^2 Score:", model.score(X_test, y_test))
