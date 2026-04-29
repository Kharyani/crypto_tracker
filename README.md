# 🚀 Live Cryptocurrency Price Tracker

## 📌 Description

This is a Python-based command-line application that fetches and displays real-time cryptocurrency prices using the CoinGecko API. The project simulates a basic fintech dashboard where users can monitor market trends and store historical price data.

---

## ✨ Features

* 📊 View live cryptocurrency prices (Bitcoin, Ethereum, etc.)
* 🔍 Search any cryptocurrency by name
* 💾 Save price history with timestamp
* 📁 Store data in JSON format
* 📜 View previously saved records
* ⚠️ Error handling for API and invalid input
* 🧩 Modular code structure

---

## 🛠 Technologies Used

* Python 3
* Requests library
* CoinGecko API
* JSON (for data storage)

---

## ⚙️ Installation

1. Clone or download the project
2. Install required library:

```bash
pip install requests
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧭 Menu Options

1. View Live Prices
2. Search Coin
3. Save Data
4. View History
5. Exit

---

## 📊 Sample Output

```
Coin: BITCOIN
Price: $76,950.00
24h Change: 0.12%
Market Cap: $1,539,918,950,833
```

---

## 📂 Data Storage

* Data is stored in `history.json`
* Each record contains:

  * Coin name
  * Price
  * Timestamp

---

## ⚠️ Error Handling

* Handles API failures
* Handles invalid coin names
* Handles missing or empty data files

---

## 🚀 Future Improvements

* GUI dashboard (Tkinter)
* Price alert system
* Graph visualization using matplotlib
* Auto-refresh feature
* Portfolio tracking

---

## 📌 API Used

* CoinGecko API (Free, no API key required)

---

## 👨‍💻 Author

Kashish Haryani

---

## 📜 License

This project is for educational purposes.
