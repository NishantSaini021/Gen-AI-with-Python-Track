# Task 3: Product Pricing (Dictionaries)
# 1. Create a dictionary price_dict where keys are product names and values are prices.
# 2. Add a new product with price.
# 3. Update the price of an existing product.
# 4. Remove a product by name (handle the case when the product does not exist).
# 5. Print the average price of all products.
# Extra (Optional): Print the product with both the maximum and minimum prices.

price_dict = {
    "Laptop": 55000,
    "Mouse": 500,
    "Keyboard": 1200,
    "Monitor": 10000,
    "Printer": 8000,
    "Speaker": 2500
}

price_dict["Webcam"] = 1500

price_dict["Mouse"] = 600

product_to_remove = "Printer"

if product_to_remove in price_dict:
    del price_dict[product_to_remove]
    print(product_to_remove, "removed successfully.")
else:
    print(product_to_remove, "not found.")

average_price = sum(price_dict.values()) / len(price_dict)

print("Average Price:", average_price)

#Extra : 
max_product = max(price_dict, key=price_dict.get)
min_product = min(price_dict, key=price_dict.get)

print("Maximum Price Product:", max_product, "-", price_dict[max_product])
print("Minimum Price Product:", min_product, "-", price_dict[min_product])