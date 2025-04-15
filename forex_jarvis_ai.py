import requests
import matplotlib.pyplot as plt
import datetime

# Replace with your actual API key
API_KEY = "3f48b8948be87f31fd483d3dc9e6326d"

def get_forex_rate(from_currency, to_currency):
    """Fetches the latest forex exchange rate."""
    url = f"https://api.exchangerate.host/latest?base={from_currency}&symbols={to_currency}&access_key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "rates" in data:
            return data['rates'].get(to_currency, None)
        else:
            print(f"Error: API response does not contain 'rates'. Full response: {data}")
            return None
    else:
        print(f"Error: Failed to fetch data. HTTP Status: {response.status_code}")
        return None


def get_historical_data(from_currency, to_currency):
    """Fetches historical forex data for the last 30 days."""
    start_date = (datetime.date.today() - datetime.timedelta(days=30)).isoformat()
    end_date = datetime.date.today().isoformat()
    url = f"https://api.exchangerate.host/timeseries?start_date={start_date}&end_date={end_date}&base={from_currency}&symbols={to_currency}&access_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "rates" in data:
            rates = data["rates"]
            dates = sorted(rates.keys())
            values = [rates[date][to_currency] for date in dates]
            return dates, values
    return None, None

def plot_forex_chart(from_currency, to_currency):
    """Plots a forex exchange rate chart for the last 30 days."""
    dates, values = get_historical_data(from_currency, to_currency)
    if dates and values:
        plt.figure(figsize=(10, 5))
        plt.plot(dates, values, marker='o', linestyle='-')
        plt.xlabel("Date")
        plt.ylabel(f"Exchange Rate ({from_currency}/{to_currency})")
        plt.title(f"{from_currency} to {to_currency} - Last 30 Days")
        plt.xticks(rotation=45)
        plt.grid()
        plt.show()
    else:
        print("Could not fetch historical data. Check your API key or currency pair.")

def answer_question(question):
    """Provides answers to common forex-related questions."""
    forex_knowledge = {
        "what is a pip": "A pip (percentage in point) is the smallest price movement in forex, usually the fourth decimal place in most currency pairs. For example, if EUR/USD moves from 1.1000 to 1.1005, that’s a 5-pip movement. In JPY pairs, the second decimal place is considered a pip.",
        "what is leverage": "Leverage allows traders to control a large position with a small deposit. For example, 1:100 leverage means you can control $10,000 with just $100. However, leverage increases both potential profits and risks.",
        "what is spread": "The spread is the difference between the bid (selling) and ask (buying) price of a currency pair. A lower spread means lower trading costs.",
    }
    return forex_knowledge.get(question.lower(), "I'm not sure about that. Can you ask something related to forex?")

def forex_chatbot():
    """Simple Forex chatbot for getting exchange rates, charts, and answering questions."""
    print("\nForex Chatbot: Type 'EXIT' to quit.")
    while True:
        user_input = input("Enter a forex question, currency pair (e.g., USD EUR), or type 'CHART USD EUR': ").strip().upper()
        
        if user_input == "EXIT":
            print("Goodbye!")
            break
        
        words = user_input.split()
        
        if len(words) == 2:  # User entered a currency pair
            from_currency, to_currency = words
            rate = get_forex_rate(from_currency, to_currency)
            if rate:
                print(f"1 {from_currency} = {rate:.6f} {to_currency}")
            else:
                print("Invalid currency pair or API issue.")
        elif len(words) == 3 and words[0] == "CHART":  # User requested a chart
            from_currency, to_currency = words[1], words[2]
            plot_forex_chart(from_currency, to_currency)
        else:
            print(answer_question(user_input))

if __name__ == "__main__":
    forex_chatbot()

