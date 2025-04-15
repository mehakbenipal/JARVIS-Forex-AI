import requests

# Your Fixer API Key
API_KEY = "3f48b8948be87f31fd483d3dc9e6326d"  # Replace with your actual key

# API Endpoint
url = f"https://data.fixer.io/api/latest?access_key={API_KEY}"

# Fetch data from Fixer API
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Check if request was successful
if data.get("success"):
    print("Exchange Rates (Base: EUR):")
    for currency, rate in data["rates"].items():
        print(f"{currency}: {rate}")
else:
    print("Error:", data.get("error", "Unknown Error"))
