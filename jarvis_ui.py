import streamlit as st
import pandas as pd
import numpy as np
import datetime
from tensorflow.keras.models import load_model  # ✅ Updated import
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Load your trained model
model = load_model("your_model.h5")  # 🔁 Replace with your model filename

# Load your dataset (for example)
data = pd.read_csv("forex_data.csv")  # 🔁 Replace with your data file
scaler = MinMaxScaler(feature_range=(0, 1))

# Preprocess data (example - customize this to your model)
scaled_data = scaler.fit_transform(data[['Close']])  # Assuming you're predicting 'Close' price

# Streamlit UI
st.set_page_config(page_title="JARVIS Forex Assistant", layout="wide")
st.title("🤖 JARVIS - Your Forex AI Assistant")
st.markdown("---")

# Input section
st.subheader("📈 Predict Next Price")
window_size = 60  # Adjust based on how your model was trained

if len(scaled_data) > window_size:
    last_window = scaled_data[-window_size:]
    x_input = np.array(last_window).reshape(1, window_size, 1)

    # Make prediction
    prediction = model.predict(x_input)
    predicted_price = scaler.inverse_transform(prediction)[0][0]

    st.success(f"💵 Predicted Next Price: **{predicted_price:.5f}**")
else:
    st.warning("Not enough data for prediction.")

# Optional: Show chart
st.subheader("📊 Price Chart")
st.line_chart(data['Close'])

# Footer
st.markdown("---")
st.caption("Made with 💖 by You & JARVIS")

