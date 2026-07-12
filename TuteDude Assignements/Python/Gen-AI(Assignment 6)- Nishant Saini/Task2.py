# Task 2. Bill Calculator with Error Handling

prices = [120, 350, 'abc', 500, -200, 800]
total = 0
for price in prices:
    try:
        if price < 0:
            raise ValueError("Negative price not allowed")
        total += price
    except TypeError:
        print("Invalid Price")
    except ValueError as e:
        print(e)
print(total)