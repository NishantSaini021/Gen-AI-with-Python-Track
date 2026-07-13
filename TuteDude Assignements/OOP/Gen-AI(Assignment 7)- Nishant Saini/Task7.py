# Task 7. Mini Project: Simple Inventory System(OOP Only)
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def get_info(self):
        print(f"Product: {self.name} | Price: {self.price} | Category: {self.category}")
        
class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        pass

    def remove_product(self,name):
        pass

    def get_total_value(self):
        pass

    def show_all_products(self):
        pass

class Store:
    def __init__(self,store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        pass
    def show_summary(self):
        pass
