import pandas as pd
import matplotlib.pyplot as plt

# Load data
forex_data = pd.read_json('USD_forex_data.json')

# Calculate daily returns
forex_data['Return'] = forex_data['Exchange Rate'].pct_change()

# Define strategy with RSI (Relative Strength Index)
def calculate_rsi(data, period=14):
    delta = data.diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Add RSI to data
forex_data['RSI'] = calculate_rsi(forex_data['Exchange Rate'])

# Define strategy: Buy when RSI < 30 (oversold), Sell when RSI > 70 (overbought)
forex_data['Signal'] = 0
forex_data.loc[forex_data['RSI'] < 30, 'Signal'] = 1
forex_data.loc[forex_data['RSI'] > 70, 'Signal'] = -1

# Calculate strategy returns
forex_data['Strategy Return'] = forex_data['Signal'].shift(1) * forex_data['Return']

# Calculate cumulative returns
forex_data['Market Cumulative'] = (1 + forex_data['Return']).cumprod()
forex_data['Strategy Cumulative'] = (1 + forex_data['Strategy Return']).cumprod()

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(forex_data['Date'], forex_data['Market Cumulative'], color='b', linewidth=2, label='Market Returns')
plt.plot(forex_data['Date'], forex_data['Strategy Cumulative'], color='orange', linewidth=2, label='Strategy Returns')
plt.title('Backtest: Strategy vs Market Performance')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.show()