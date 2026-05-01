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

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "bitcoin" not in data:
            return "Bitcoin data unavailable. Please refresh later."

        price = data["bitcoin"]["usd"]
        change = data["bitcoin"]["usd_24h_change"]

        return render_template(
            "btc.html",
            price=round(price, 2),
            change=round(change, 2)
        )

    except Exception as e:
        return f"CoinGecko API error: {str(e)}"
