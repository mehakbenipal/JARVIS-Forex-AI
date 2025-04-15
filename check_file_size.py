import os

file_path = "USD_forex_data.json"
if os.path.getsize(file_path) == 0:
    print("❌ The file is empty!")
else:
    print(f"✅ File size: {os.path.getsize(file_path)} bytes")
