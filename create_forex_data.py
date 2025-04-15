import pandas as pd

# New correct forex data
data = {
    "Date": ["2025-03-01", "2025-03-02", "2025-03-03", "2025-03-04", "2025-03-05"],
    "Exchange Rate": [0.9215, 0.9216, 0.9218, 0.9220, 0.9223]
}

# Save as CSV (this will overwrite the old file)
df = pd.DataFrame(data)
df.to_csv("forex_data.csv", index=False)

print("New forex_data.csv file has been created!")
