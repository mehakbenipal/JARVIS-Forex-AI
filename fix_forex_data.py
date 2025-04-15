import pandas as pd

# Load data
df = pd.read_csv("forex_data.csv")  # Replace with your actual filename

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# Save the fixed data
df.to_csv("forex_data_final.csv", index=False)

print("✅ Date column properly converted and saved as 'forex_data_final.csv'!")

print(df.head())  # Print first few rows to verify date conversion
