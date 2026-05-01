import time

cache = {}
CACHE_TIME = 30 

@app.route("/btc")
def btc():
    global cache

    # check cache first
    if "btc" in cache:
        if time.time() - cache["btc"]["time"] < CACHE_TIME:
            data = cache["btc"]["data"]
            return render_template(
                "btc.html",
                price=round(data["bitcoin"]["usd"], 2),
                change=round(data["bitcoin"]["usd_24h_change"], 2)
            )

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        # save to cache
        cache["btc"] = {
            "time": time.time(),
            "data": data
        }

        return render_template(
            "btc.html",
            price=round(data["bitcoin"]["usd"], 2),
            change=round(data["bitcoin"]["usd_24h_change"], 2)
        )

    except Exception as e:
        return f"CoinGecko API error: {str(e)}"
