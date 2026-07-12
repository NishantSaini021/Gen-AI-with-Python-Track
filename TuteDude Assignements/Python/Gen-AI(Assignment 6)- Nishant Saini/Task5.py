# Task 5. Mini Program: Safe Shopping Cart
class NegativePriceError(Exception):
    pass

cart = []

while True:
    print("To exit press q")
    price = input("Enter Price: ")

    if price == "q":
        print(f"\nTotal Items: {len(cart)}")
        print(f"Total Bill: {sum(cart)}")
        break

    try:
        price = float(price)

        if price < 0:
            raise NegativePriceError("Negative Price not allowed")

        cart.append(price)

    except ValueError:
        print("Invalid Input")

    except NegativePriceError as e:
        print(e)