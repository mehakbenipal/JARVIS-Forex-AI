# retrain_models.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
import joblib
import os

# Load latest forex data
df = pd.read_csv("forex_data.csv")

# Detect date column
date_col = None
for col in df.columns:
    if "date" in col.lower() or "time" in col.lower():
        date_col = col
        break

if date_col:
    df['timestamp'] = pd.to_datetime(df[date_col])
    df.set_index('timestamp', inplace=True)
else:
    print("❌ Could not find a timestamp/date column!")

# --- Train & Save Random Forest ---
def train_random_forest(data):
    X, y, scaler = prepare_data_for_model(data)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, "models/random_forest.pkl")
    joblib.dump(scaler, "models/rf_scaler.pkl")
    print("✅ Random Forest saved!")

# --- Train & Save XGBoost ---
def train_xgboost(data):
    X, y, scaler = prepare_data_for_model(data)
    model = XGBRegressor(n_estimators=100, learning_rate=0.05)
    model.fit(X, y)
    joblib.dump(model, "models/xgboost.pkl")
    joblib.dump(scaler, "models/xgb_scaler.pkl")
    print("✅ XGBoost saved!")

# --- Train & Save LSTM ---
def train_lstm(data):
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data.reshape(-1, 1))
    
    X = []
    sequence_length = 60
    for i in range(sequence_length, len(scaled_data)):
        X.append(scaled_data[i-sequence_length:i, 0])
    X = np.array(X)
    X = X.reshape((X.shape[0], X.shape[1], 1))
    
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1), name="lstm_1"))
    model.add(LSTM(50, name="lstm_2"))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X, scaled_data[sequence_length:], epochs=5, batch_size=32, verbose=0)

    model.save("models/lstm_model.h5")
    joblib.dump(scaler, "models/lstm_scaler.pkl")
    print("✅ LSTM saved!")

# --- Data Preparer ---
def prepare_data_for_model(data, look_back=60):
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(data.reshape(-1, 1))
    X, y = [], []
    for i in range(look_back, len(scaled)):
        X.append(scaled[i-look_back:i])
        y.append(scaled[i])
    X = np.array(X)
    y = np.array(y)
    X_flat = X.reshape(X.shape[0], -1)
    return X_flat, y, scaler

# 💾 Retrain All
if not os.path.exists("models"):
    os.makedirs("models")

close_data = df['Close'].dropna().values
train_random_forest(close_data)
train_xgboost(close_data)
train_lstm(close_data)

print("🎉 All models retrained and saved successfully!")
