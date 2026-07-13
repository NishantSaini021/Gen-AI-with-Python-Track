# Task 7. Mini Project: Simple Inventory System(OOP Only)
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def get_info(self):
        print(f"Product: {self.name} | Price: {self.price} | Category: {self.category}")
    def __add__(self, other):
        return self.price + other.price
        
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)

    def remove_product(self,name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_all_products(self):
        for product in self.products:
            product.get_info()

class Store:
    def __init__(self,store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Enter name of Product: ")
        while True:
            try:
                price = int(input("Enter price of product: "))
                break
            except ValueError:
                print("Invalid Price")
        category = input("Category of Product: ")
        product = Product(name,price,category)
        self.inventory.add_product(product)
    def show_summary(self):
        print(f"Store Name: {self.store_name}")
        print(f"Total Products: {len(self.inventory.products)}")
        print(f"Total Inventory Value: {self.inventory.get_total_value()}")


store = Store("XYZ Electronics")
store.add_new_product()
store.add_new_product()
store.add_new_product()
store.inventory.show_all_products()
store.show_summary()