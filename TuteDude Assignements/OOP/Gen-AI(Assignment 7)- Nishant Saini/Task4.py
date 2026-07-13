# Task 4. Polymorphism
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def get_info(self):
        print(f"Product: {self.name} | Price: {self.price} | Category: {self.category}")


class Laptop(Product):
    def __init__(self,name,price,category,warranty):
        Product.__init__(self,name,price,category)
        self.warranty = warranty
    def get_info(self):
        print(f"Name: {self.name}\nPrice: {self.price}\nCategory: {self.category}\nWarranty: {self.warranty}")

class Mobile(Product):
    def __init__(self,name,price,category,storage):
        Product.__init__(self,name,price,category)
        self.storage = storage
    def get_info(self):
        print(f"1.Name: {self.name}   Category: {self.category}\n2.Storage: {self.storage}   Price: {self.price}")


m1 = Mobile("Samsung S23", 80000, "Android", "16GB RAM")
m2 = Mobile("Samsung S26 Ultra", 130000, "Android", "16GB RAM")
l1 = Laptop("Apple Macbook Neo", 69000, "MacOS", "1 Year with apple care")
l2 = Laptop("Apple Macbook M4 Pro", 129000, "MacOS", "1 Year with apple care")

products = [m1,m2,l1,l2]
for product in products:
    product.get_info()