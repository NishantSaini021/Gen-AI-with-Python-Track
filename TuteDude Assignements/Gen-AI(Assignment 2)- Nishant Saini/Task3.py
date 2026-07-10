orders = []

while True:
    print("\nMenu")
    print("1 - Add Order Amount")
    print("2 - Show Orders and Totals")
    print("q - Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter order amount: "))
            orders.append(amount)
            print("Order added.")
        except ValueError:
            print("Invalid amount.")
            continue

    elif choice == "2":

        if len(orders) == 0:
            print("No orders available.")
            continue

        total = 0

        print("\nOrders Summary")

        for order in orders:

            if order >= 2000:
                discount = 15
            elif order >= 1500:
                discount = 10
            elif order >= 1000:
                discount = 7
            else:
                discount = 0

            final_amount = order - ((order * discount) / 100)

            total += final_amount

            print("Order:", order,
                  "Discount:", discount,
                  "Final:", final_amount)

        print("Total Revenue:", total)

    elif choice.lower() == "q":
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")
        continue