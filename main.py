from api import fetch_crypto_data
from storage import save_data, view_history
from utils import format_output

def main():
    coins = ["bitcoin", "ethereum"]

    while True:
        print("\n===== CRYPTO TRACKER =====")
        print("1. View Live Prices")
        print("2. Search Coin")
        print("3. Save Data")
        print("4. View History")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            data = fetch_crypto_data(coins)
            if data:
                format_output(data)

        elif choice == "2":
            coin = input("Enter coin name: ").lower()
            data = fetch_crypto_data([coin])

            if data and coin in data:
                format_output(data)
            else:
                print("❌ Coin not found!")

        elif choice == "3":
            data = fetch_crypto_data(coins)
            if data:
                save_data(data)

        elif choice == "4":
            view_history()

        elif choice == "5":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()