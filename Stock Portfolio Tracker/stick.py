import csv
from datetime import datetime

# Hardcoded stock prices (dictionary)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 330,
}


def show_available_stocks():
    print("Available stocks and current prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price}")
    print()


def get_portfolio():
    """Ask the user for stock symbols and quantities until they're done."""
    portfolio = {}  # symbol -> quantity

    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in our price list. Please choose from the list above.\n")
            continue

        qty_input = input(f"Enter quantity of {symbol}: ").strip()
        if not qty_input.isdigit():
            print("Please enter a valid whole number for quantity.\n")
            continue

        quantity = int(qty_input)
        if quantity <= 0:
            print("Quantity must be greater than zero.\n")
            continue

        # If the stock was already entered, add to the existing quantity
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.\n")

    return portfolio


def calculate_investment(portfolio):
    """Return a list of (symbol, quantity, price, value) rows and the total."""
    rows = []
    total = 0
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        rows.append((symbol, quantity, price, value))
        total += value
    return rows, total


def display_summary(rows, total):
    print("\n----- Portfolio Summary -----")
    print(f"{'Symbol':<10}{'Quantity':<10}{'Price':<10}{'Value':<10}")
    for symbol, quantity, price, value in rows:
        print(f"{symbol:<10}{quantity:<10}${price:<9}${value:<9}")
    print("-" * 40)
    print(f"Total Investment Value: ${total}")
    print("-" * 40)


def save_to_txt(rows, total, filename="portfolio_summary.txt"):
    with open(filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-" * 40 + "\n")
        f.write(f"{'Symbol':<10}{'Quantity':<10}{'Price':<10}{'Value':<10}\n")
        for symbol, quantity, price, value in rows:
            f.write(f"{symbol:<10}{quantity:<10}${price:<9}${value:<9}\n")
        f.write("-" * 40 + "\n")
        f.write(f"Total Investment Value: ${total}\n")
    print(f"Saved summary to {filename}")


def save_to_csv(rows, total, filename="portfolio_summary.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price", "Value"])
        for symbol, quantity, price, value in rows:
            writer.writerow([symbol, quantity, price, value])
        writer.writerow([])
        writer.writerow(["Total Investment Value", "", "", total])
    print(f"Saved summary to {filename}")


def main():
    print("=== Stock Portfolio Tracker ===\n")
    show_available_stocks()

    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    rows, total = calculate_investment(portfolio)
    display_summary(rows, total)

    choice = input("\nSave summary to a file? (y/n): ").lower().strip()
    if choice == "y":
        file_type = input("Save as 'txt' or 'csv'? ").lower().strip()
        if file_type == "csv":
            save_to_csv(rows, total)
        else:
            save_to_txt(rows, total)
    else:
        print("Summary not saved.")


if __name__ == "__main__":
    main()