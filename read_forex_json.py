import json

file_path = "USD_forex_data.json"

with open(file_path, 'r') as file:
    data = json.load(file)
    print(json.dumps(data, indent=4))  # Nicely formatted output
