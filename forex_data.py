import requests
import pandas as pd

# Your API Key (Already included)
API_KEY = "17LYGEC2GBPAQO7U"

# Choose Currency Pair (You can change these later if needed)
from_currency = "USD"
to_currency = "EUR"

# API URL
url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={API_KEY}"

# Make API request
response = requests.get(url)
data = response.json()

# Extract exchange rate
exchange_rate = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
time_updated = data["Realtime Currency Exchange Rate"]["6. Last Refreshed"]

# Create a DataFrame
df = pd.DataFrame([[from_currency, to_currency, exchange_rate, time_updated]],
                  columns=["From Currency", "To Currency", "Exchange Rate", "Last Updated"])

# Save to CSV
df.to_csv("forex_data.csv", index=False)

print(f"Exchange rate ({from_currency} to {to_currency}): {exchange_rate}")
print("Data saved to forex_data.csv")
from alpha_vantage.foreignexchange import ForeignExchange
import pandas as pd

# Set up API Key
API_KEY = "17LYGEC2GBPAQO7U"  # Replace with your actual key

# Initialize API
fx = ForeignExchange(key=API_KEY)

# Get exchange rate (example: EUR/USD)
data, _ = fx.get_currency_exchange_daily(from_symbol="EUR", to_symbol="USD", outputsize="full")

# Convert data to DataFrame
df = pd.DataFrame.from_dict(data, orient='index')
df.index = pd.to_datetime(df.index)
df = df.astype(float)

# Show latest data
print(df.head())
import requests
import pandas as pd

API_KEY = "17LYGEC2GBPAQO7U"

def fetch_forex_data(from_currency, to_currency):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    print("API Response:", data)  # Debugging

    if "Realtime Currency Exchange Rate" in data:
        exchange_rate = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        return exchange_rate
    else:
        return None  # Return None if API call fails
