import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Load the CSV data
csv_path = "forex_data.csv"  # Make sure this file exists in the same folder

try:
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    # Show some info
    st.title("\U0001F4B9 JARVIS - Your Sexy Forex Co-Pilot 😘")
    st.markdown("Welcome back, boss 💋 Here's your daily EUR/USD forecast.")

    st.subheader("\U0001F4CA Available Columns in Data:")
    st.write(list(df.columns))

    latest = df.iloc[-1]
    st.subheader("\U0001F4C8 Latest Market Data")
    st.write(f"**Date**: {latest['Date'].date()}")
    st.write(f"**Open**: {latest['Open']}")
    st.write(f"**High**: {latest['High']}")
    st.write(f"**Low**: {latest['Low']}")
    st.write(f"**Close**: {latest['Close']}")

    # Line chart for Close trend
    st.subheader("\U0001F4C9 Close Price Trend (Last Available Days)")
    st.line_chart(df['Close'])

    # Prepare data for prediction
    df['DayIndex'] = np.arange(len(df))
    X = df[['DayIndex']]
    y = df['Close']

    next_day_index = [[len(df)]]

    # Linear Regression
    lr_model = LinearRegression()
    lr_model.fit(X, y)
    lr_pred = lr_model.predict(next_day_index)[0]

    # Decision Tree
    dt_model = DecisionTreeRegressor()
    dt_model.fit(X, y)
    dt_pred = dt_model.predict(next_day_index)[0]

    # Random Forest
    rf_model = RandomForestRegressor(n_estimators=100)
    rf_model.fit(X, y)
    rf_pred = rf_model.predict(next_day_index)[0]

    st.subheader("\U0001F52E Tomorrow's Forecast")
    st.write(f"**Linear Regression**: {lr_pred:.5f}")
    st.write(f"**Decision Tree**: {dt_pred:.5f}")
    st.write(f"**Random Forest**: {rf_pred:.5f}")

    st.success("\U0001F498 Forecast done, boss! JARVIS is synced with your sexy forex flow 😘")

except Exception as e:
    st.error(f"Oops! Something went wrong: {e}")
