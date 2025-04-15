import requests
import json

API_KEY = "2b1cfa88bd54d3ed7f7480a6"  # Replace with your actual API key
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def fetch_and_save_forex_data(base_currency="USD"):
    url = BASE_URL + base_currency
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["result"] == "success":
            print(f"✅ Exchange rates for {base_currency} fetched successfully!")

            # Save to JSON file
            with open(f"{base_currency}_forex_data.json", "w") as json_file:
                json.dump(data, json_file, indent=4)

            print(f"📂 Data saved to {base_currency}_forex_data.json")
        else:
            print("❌ Error:", data["error-type"])
    else:
        print("❌ Failed to fetch forex data. HTTP Status Code:", response.status_code)

# Example usage
fetch_and_save_forex_data("USD")  # You can change "USD" to any currency
