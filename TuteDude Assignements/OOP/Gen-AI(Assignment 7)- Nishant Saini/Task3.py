# Task 3. Inheritance(Single-Level)

class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def get_info(self):
        print(f"Product: {self.name} | Price: {self.price} | Category: {self.category}")

class ElectronicProduct(Product):
    def __init__(self,name,price,category,warranty_years):
        Product.__init__(self,name, price, category)
        self.warranty_years = warranty_years
    def get_info(self):
        print(f"Product: {self.name} | Price: {self.price} | Category: {self.category} | Warranty Info: {self.warranty_years}")

p1 = ElectronicProduct("CPU", 25000, "Computer Parts", "2 Years")
p1.get_info()
