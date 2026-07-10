# Using Filter(): Filter Expensive Products 
prices = [100, 250, 400, 1200, 50, 2000, 850]
expensive_products_filter = lambda x: x > 500
cheap_products_filter = lambda x: x <= 500
expensive_products = filter(expensive_products_filter, prices)
cheap_products = filter(cheap_products_filter, prices)

print(f"Expensive Products Price: {list(expensive_products)}")
print(f"Cheaper Products Price: {list(cheap_products)}")
