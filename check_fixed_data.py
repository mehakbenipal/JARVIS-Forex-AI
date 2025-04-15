import pandas as pd

df = pd.read_csv("forex_data_final.csv")
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')  # Convert Date column
print(df.dtypes)  # Check data types again


# Check data types
print(df.dtypes)
