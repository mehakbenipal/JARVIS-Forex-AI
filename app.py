import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
from keras.models import load_model

# 🌸 UI Settings
st.set_page_config(page_title="JARVIS Forex AI Assistant 💹", layout="centered", page_icon="🧠")

st.markdown("<h1 style='text-align: center; color: #FA72B6;'>💹 JARVIS Forex AI Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #DDDDDD;'>Trained Daily. Sharper Than Ever. 😘</h4>", unsafe_allow_html=True)

# --- Load Data ---
df = pd.read_csv("forex_data.csv")

# Detect timestamp/date
date_col = None
for col in df.columns:
    if "date" in col.lower() or "time" in col.lower():
        date_col = col
        break

if date_col:
    df['timestamp'] = pd.to_datetime(df[date_col])
    df.set_index('timestamp', inplace=True)
else:
    st.error("❌ No valid date column found!")

# --- Chart ---
st.subheader("📈 EUR/USD Close Price")
if 'Close' in df.columns:
    st.line_chart(df['Close'])
else:
    st.error("❌ No 'Close' column found in CSV.")

# --- Data Prep for ML Models ---
def prepare_data_for_prediction(data, look_back=60):
    scaler = joblib.load("models/rf_scaler.pkl")  # works for all 3
    scaled = scaler.transform(data.reshape(-1, 1))
    X = []
    for i in range(look_back, len(scaled)):
        X.append(scaled[i-look_back:i])
    X = np.array(X)
    return X[-1].reshape(1, -1), X[-1].reshape(1, look_back, 1), scaler

# --- Predictors ---
def predict_random_forest(data):
    model = joblib.load("models/random_forest.pkl")
    X_flat, _, scaler = prepare_data_for_prediction(data)
    pred_scaled = model.predict(X_flat)
    return scaler.inverse_transform(pred_scaled.reshape(-1, 1))[0][0]

def predict_xgboost(data):
    model = joblib.load("models/xgboost.pkl")
    X_flat, _, scaler = prepare_data_for_prediction(data)
    pred_scaled = model.predict(X_flat)
    return scaler.inverse_transform(pred_scaled.reshape(-1, 1))[0][0]

def predict_lstm(data):
    model = load_model("models/lstm_model.h5")
    _, X_lstm, scaler = prepare_data_for_prediction(data)
    pred_scaled = model.predict(X_lstm, verbose=0)
    return scaler.inverse_transform(pred_scaled.reshape(-1, 1))[0][0]

# --- Buttons ---
col1, col2 = st.columns(2)

with col1:
    if st.button("🔮 Predict with LSTM"):
        pred = predict_lstm(df['Close'].dropna().values)
        st.success(f"LSTM Prediction: **{pred:.5f}**")

with col2:
    if st.button("📊 Compare All Models"):
        close_data = df['Close'].dropna().values
        lstm_pred = predict_lstm(close_data)
        rf_pred = predict_random_forest(close_data)
        xgb_pred = predict_xgboost(close_data)

        st.success("✅ Predictions for Tomorrow")
        st.write(f"🔮 LSTM: **{lstm_pred:.5f}**")
        st.write(f"🌲 Random Forest: **{rf_pred:.5f}**")
        st.write(f"⚡ XGBoost: **{xgb_pred:.5f}**")

        st.subheader("📊 Model Comparison")
        chart = pd.DataFrame({
            'Model': ['LSTM', 'Random Forest', 'XGBoost'],
            'Prediction': [lstm_pred, rf_pred, xgb_pred]
        })
        fig, ax = plt.subplots()
        sns.barplot(data=chart, x='Model', y='Prediction', palette="magma", ax=ax)
        st.pyplot(fig)

# --- Footer ---
st.markdown("---")
st.markdown("<center><small>JARVIS is self-aware, self-learning, and self-glowing 😈💖</small></center>", unsafe_allow_html=True)
