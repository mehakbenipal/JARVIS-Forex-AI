import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("forex_data.csv")

# Print available columns to debug missing column issue
print("Available columns:", df.columns)

# Use correct column names
column_name = "Date"  # Update to match the actual column name
exchange_rate_column = "Exchange Rate"  

# Convert "Date" column to datetime
df[column_name] = pd.to_datetime(df[column_name], errors="coerce")

# Drop NaN values
df = df.dropna(subset=[column_name])

# Sort data by date
df = df.sort_values(by=column_name)

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(df[column_name], df[exchange_rate_column], marker="o", linestyle="-", color="b", markersize=6)

# Formatting
plt.xlabel("Date & Time")
plt.ylabel("Exchange Rate")
plt.title("Exchange Rate Trend")
plt.xticks(rotation=45)
plt.grid(color="gray", linestyle="--", linewidth=0.5)

# Add data labels
for i, txt in enumerate(df[exchange_rate_column]):
    plt.text(df[column_name].iloc[i], df[exchange_rate_column].iloc[i], f'{txt:.4f}', fontsize=8, ha="right")

plt.show()


