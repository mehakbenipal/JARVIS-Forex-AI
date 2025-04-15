import requests
import pandas as pd
from datetime import datetime

# Replace with your Forex API key
API_KEY = "3f48b8948be87f31fd483d3dc9e6326d"

# Currency pair (e.g., EUR/USD)
BASE_CURRENCY = "EUR"
QUOTE_CURRENCY = "USD"

# API URL (Example: Use a real forex API provider)
API_URL = API_URL = f"https://api.exchangerate.host/latest?base=EUR&symbols=USD"

def fetch_forex_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        if "rates" in data:
            forex_data = [
                {"date": date, "price": rates[QUOTE_CURRENCY]}
                for date, rates in data["rates"].items()
            ]
            return pd.DataFrame(forex_data)
        else:
            print("Invalid response data")
            return None
    else:
        print("Failed to fetch data:", response.status_code)
        return None

# Fetch data and save to CSV
df = fetch_forex_data()
if df is not None:
    df.to_csv("forex_data.csv", index=False)
    print("Forex data saved to forex_data.csv")
