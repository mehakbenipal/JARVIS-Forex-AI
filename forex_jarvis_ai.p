import requests

def get_forex_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['rates'].get(to_currency, None)
    return None

def answer_question(question):
    forex_knowledge = {
        "what is a pip": "A pip (percentage in point) is the smallest price movement in forex, usually the fourth decimal place in most currency pairs. For example, if EUR/USD moves from 1.1000 to 1.1005, that’s a 5-pip movement. In JPY pairs, the second decimal place is considered a pip.",
        "what is leverage": "Leverage allows traders to control a large position with a small deposit. For example, 1:100 leverage means you can control $10,000 with just $100. However, leverage increases both potential profits and risks.",
        "what is spread": "The spread is the difference between the bid (selling) and ask (buying) price of a currency pair. A lower spread means lower trading costs.",
    }
    return forex_knowledge.get(question.lower(), "I'm not sure about that. Can you ask something related to forex?")

def forex_chatbot():
    print("\nForex Chatbot: Type 'EXIT' to quit.")
    while True:
        user_input = input("Enter a forex question or currency pair (e.g., USD EUR): ").strip().upper()
        
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
        else:
            print(answer_question(user_input))

if __name__ == "__main__":
    forex_chatbot()
