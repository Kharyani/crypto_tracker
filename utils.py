def format_output(data):
    print("\n📊 Live Crypto Prices:\n")
    print("-" * 40)

    for coin, details in data.items():
        print(f"Coin: {coin.upper()}")
        print(f"Price: ${details['usd']:,.2f}")
        print(f"24h Change: {details['usd_24h_change']:.2f}%")
        print(f"Market Cap: ${details['usd_market_cap']:,.0f}")
        print("-" * 40)