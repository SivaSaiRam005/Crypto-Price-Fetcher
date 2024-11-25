import requests

def get_bitcoin_price():
    # Binance API endpoint for fetching Bitcoin price
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    
    try:
        # Sending GET request to the Binance API
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        
        # Parse JSON response
        data = response.json()
        price = data["price"]
        
        return f"Current Bitcoin Price: ${price}"
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching Bitcoin price: {e}"

if __name__ == "__main__":
    print(get_bitcoin_price())
