import pandas as pd

# Load your forex data
df = pd.read_csv("forex_data.csv")  # Change filename if needed

# Check for missing values
print(df.isnull().sum())

# Check data types
print(df.dtypes)

# Preview data
print(df.head())
