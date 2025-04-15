import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# Load exchange rate data
forex_data = pd.read_csv("forex_data.csv")  # Change if using JSON

# Convert Date column to datetime format for better plotting
forex_data["Date"] = pd.to_datetime(forex_data["Date"])

# Set the style for better visuals
sns.set_theme(style="whitegrid")

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(forex_data["Date"], forex_data["Exchange Rate"], marker="o", linestyle="-", color="b", linewidth=2, markersize=5, label="Exchange Rate")

# Format the x-axis labels
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

# Add labels and title
plt.xlabel("Date", fontsize=12)
plt.ylabel("Exchange Rate", fontsize=12)
plt.title("Exchange Rate Trend", fontsize=14, fontweight='bold')

# Add value labels to points
for i, txt in enumerate(forex_data["Exchange Rate"]):
    plt.annotate(f"{txt:.4f}", (forex_data["Date"][i], forex_data["Exchange Rate"][i]), textcoords="offset points", xytext=(0, 5), ha="center")

# Show legend
plt.legend()

# Show the plot
plt.show()
