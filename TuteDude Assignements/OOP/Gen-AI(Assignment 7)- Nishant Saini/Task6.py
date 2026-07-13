# Task 6. Magic Method and Operator Overloading

class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nCategory: {self.category}"
    def __add__(self,other):
        return self.price + other.price
    
p1 = Product("Mouse", 300, "Electronics")
p2 = Product("Monitor", 12000, "Electronics")

print(p1)
print(p1+p2)