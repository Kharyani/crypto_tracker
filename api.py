import requests

BASE_URL = "https://api.coingecko.com/api/v3/simple/price"

def fetch_crypto_data(coins):
    try:
        ids = ",".join(coins)
        url = f"{BASE_URL}?ids={ids}&vs_currencies=usd&include_24hr_change=true&include_market_cap=true"

        response = requests.get(url)

        if response.status_code != 200:
            print("❌ API Error!")
            return None

        return response.json()

    except Exception as e:
        print("⚠️ Error:", e)
        return None