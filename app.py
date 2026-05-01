from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Bitcoin Tracker is running 🚀 Go to /btc"

@app.route("/btc")
def btc():
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        return "CoinGecko API error. Please refresh later."

    data = response.json()
    print(data)


    if "bitcoin" not in data:
        return "Bitcoin data unavailable. Please refresh later."

    price = data["bitcoin"]["usd"]
    change = data["bitcoin"]["usd_24h_change"]

    return render_template(
        "btc.html",
        price=round(price, 2),
        change=round(change, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)
