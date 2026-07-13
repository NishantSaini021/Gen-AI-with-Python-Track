# Task 1. Basic Object and Classes

class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def get_info(self):
        print(f"Product: {self.name} | Price: {self.price} | Category: {self.category}")
    

p1 = Product("Mouse", 300, "Electronics")
p2 = Product("Monitor", 12000, "Electronics")

p1.get_info()