import json
from datetime import datetime

FILE_NAME = "history.json"

def save_data(data):
    try:
        with open(FILE_NAME, "r") as f:
            history = json.load(f)
    except:
        history = []

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for coin, details in data.items():
        history.append({
            "coin": coin,
            "price": details["usd"],
            "timestamp": timestamp
        })

    with open(FILE_NAME, "w") as f:
        json.dump(history, f, indent=4)

    print("✅ Data saved successfully!")


def view_history():
    try:
        with open(FILE_NAME, "r") as f:
            history = json.load(f)

        for record in history[-10:]:
            print(record)

    except:
        print("⚠️ No history found!")