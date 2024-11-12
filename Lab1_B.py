price = float(input("Enter the price of the item: "))
taxPercent = float(input("Enter the sales tax percentage: ")) / 100
total = (price * taxPercent) + price

print(f"Your total is ${total:.2f}")