import json
import pandas as pd

try:
    # Force read with error replacement
    with open("USD_forex_data.json", "r", encoding="utf-8", errors="replace") as file:
        raw_data = file.read()
    print("📂 Raw File Content Loaded Successfully!")

    # Parse JSON
    print(raw_data[:500])  # Print first 500 characters
    forex_data = json.loads(raw_data)
    print("✅ JSON is valid!\n")

    # Convert to DataFrame
    exchange_rates = pd.DataFrame(forex_data["conversion_rates"], index=[0]).T
    exchange_rates.columns = ["Exchange Rate"]
    print("📊 DataFrame Created:\n", exchange_rates)

except json.JSONDecodeError as e:
    print(f"❌ JSON Decoding Error: {e}")
except Exception as e:
    print(f"⚠️ Unexpected Error: {e}")
