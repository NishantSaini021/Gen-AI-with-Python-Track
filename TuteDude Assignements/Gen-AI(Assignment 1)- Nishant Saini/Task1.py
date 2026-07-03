# Task 1: Product Collections (Lists & Tuples)
# 1. Create a list named products containing at least 6 product names (strings).
# 2. Create a tuple named sample_product that stores (product_name, price, category) for one product.
# 3. Print the 2nd and last product from the products list.
# 4. Append two new product names to products and then print the updated list.
# Extra (Optional): Convert sample_product into a list, change its price, and convert it back to a tuple.

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Speaker"]

sample_product = ("Laptop", 55000, "Electronics")

print("2nd Product:", products[1])
print("Last Product:", products[-1])

products.append("Webcam")
products.append("Router")

print("Updated Products List:")
print(products)

#Extra:
sample_list = list(sample_product)
sample_list[1] = 60000
sample_product = tuple(sample_list)

print("Updated Tuple:")
print(sample_product)