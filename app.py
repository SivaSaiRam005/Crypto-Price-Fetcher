from flask import Flask, render_template
import requests

app = Flask(__name__)

def fetch_prices():
    apis = {
        "Binance": "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
        "Bitget": "https://api.bitget.com/api/spot/v1/market/tickers",
        "KuCoin": "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT",
    }

    prices = {}
    for exchange, url in apis.items():
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if exchange == "Binance":
                prices[exchange] = float(data["price"])
            elif exchange == "Bitget":
                market_data = data["data"]
                for item in market_data:
                    if item["symbol"] == "BTCUSDT":
                        prices[exchange] = float(item["close"])
                        break
            elif exchange == "KuCoin":
                prices[exchange] = float(data["data"]["price"])
        except Exception as e:
            prices[exchange] = f"Error: {e}"
    return prices



@app.route("/")
def index():
    bitcoin_prices = fetch_prices()
    return render_template("index.html", prices=bitcoin_prices)

if __name__ == "__main__":
    app.run(debug=True)
