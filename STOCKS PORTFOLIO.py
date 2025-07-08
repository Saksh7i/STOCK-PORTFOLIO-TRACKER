stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2750,
    "AMZN": 135,
    "MSFT": 330
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("⚠️ Invalid stock symbol. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity
    total_investment += stock_prices[stock] * quantity

print("\n🧾 Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\n💰 Total Investment: ${total_investment}")

save_option = input("Do you want to save this to a file? (yes/no): ").lower()
if save_option == "yes":
    filename = "portfolio_summary.txt"
    with open(filename, "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            file.write(f"{stock}: {qty} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment: ${total_investment}\n")
    print(f"✅ Portfolio saved to '{filename}'")
