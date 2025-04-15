import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/"  # Free exchange rate API

def get_exchange_rate(from_currency, to_currency, amount=1):
    try:
        response = requests.get(API_URL + from_currency.upper())
        data = response.json()
        if to_currency.upper() in data["rates"]:
            rate = data["rates"][to_currency.upper()]
            converted_amount = round(amount * rate, 2)
            return f"{amount} {from_currency.upper()} = {converted_amount} {to_currency.upper()}"
        else:
            return "Currency not found. Please try again."
    except Exception as e:
        return f"Error fetching data: {str(e)}"

def forex_chatbot():
    print("Forex Chatbot: Type a query like '100 USD to INR' or type 'help' for options. Type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "exit":
            print("Bot: Goodbye!")
            break
        elif user_input == "help":
            print("Bot: Enter a currency conversion like '100 USD to INR' or '50 EUR to GBP'.")
        else:
            try:
                parts = user_input.split()
                if len(parts) == 4 and parts[2] == "to":
                    amount = float(parts[0])
                    from_currency = parts[1].upper()
                    to_currency = parts[3].upper()
                    print("Bot:", get_exchange_rate(from_currency, to_currency, amount))
                else:
                    print("Bot: Invalid format. Try '100 USD to INR'.")
            except ValueError:
                print("Bot: Please enter a valid amount.")

if __name__ == "__main__":
    forex_chatbot()
