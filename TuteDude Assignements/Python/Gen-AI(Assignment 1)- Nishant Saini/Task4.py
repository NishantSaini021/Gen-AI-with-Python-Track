# Task 4: Combined Operations
# 1. Using the products list and price_dict, create a list of tuples named catalog
#    where each tuple is (product_name, price, category).
# 2. From catalog, create a new dictionary category_to_products that maps
#    each category to a list of product names in that category.
# 3. Print all products that belong to the category that has the maximum number of products.

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Speaker"]

price_dict = {
    "Laptop": 55000,
    "Mouse": 500,
    "Keyboard": 1200,
    "Monitor": 10000,
    "Printer": 8000,
    "Speaker": 2500
}

categories = [
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Office",
    "Audio"
]

catalog = []

for i in range(len(products)):
    catalog.append((products[i], price_dict[products[i]], categories[i]))

print("Catalog:")
for item in catalog:
    print(item)

category_to_products = {}

for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product)

print("Category to Products:")
print(category_to_products)

max_category = max(category_to_products,
                   key=lambda x: len(category_to_products[x]))

print("Category with Maximum Products:", max_category)
print("Products:")

for product in category_to_products[max_category]:
    print(product)