import requests
import csv
from datetime import datetime

# Fixer API Key (Replace with your actual API key)
API_KEY = "3f48b8948be87f31fd483d3dc9e6326d"

# Base currency (EUR by default)
BASE_CURRENCY = "EUR"

# Get forex data from Fixer API
url = f"http://data.fixer.io/api/latest?access_key={API_KEY}&base={BASE_CURRENCY}"
response = requests.get(url)
data = response.json()

# Get current date
date = datetime.now().strftime("%Y-%m-%d")

# Extract exchange rates
exchange_rates = data.get("rates", {})

# File name to save data
csv_file = "forex_data.csv"

# Save data to CSV
with open(csv_file, mode="a", newline="") as file:  # "a" means append (not overwrite)
    writer = csv.writer(file)
    
    # Write header only if the file is empty
    if file.tell() == 0:
        writer.writerow(["Date", "Currency", "Exchange Rate"])
    
    # Write exchange rates
    for currency, rate in exchange_rates.items():
        writer.writerow([date, currency, rate])

print(f"✅ Forex data saved successfully in {csv_file}!")
