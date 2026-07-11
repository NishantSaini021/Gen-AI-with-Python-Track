# Task 7. Mini Project: Export Discounted Prices

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}
discount = int(input("Enter Discount percentage: "))
avg_discount = []
with open("discount_report.txt", "w") as file:
    for product,price in prices.items():
        discounted_price = price - ((price * discount) / 100)
        file.write(f"{product}|{price}|{discounted_price}\n")
        avg_discount.append(discounted_price)
    file.write(f"Total Items: {len(prices)}\n")
    file.write(f"Average Discounted Price: {sum(avg_discount)/len(avg_discount)}\n"
)
with open("discount_report.txt", "r") as file:
    data = file.read()
print(data)
