# Task 2. Constructor and Encapsulation

class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.__price = price
        self.category = category
    def get_price(self):
        return self.__price
    def set_price(self,new_price):
        if new_price > 0 :
            self.__price = new_price
    

p1 = Product("Mouse", 300, "Electronics")
p2 = Product("Monitor", 12000, "Electronics")

p1.set_price(500)
p2.set_price(-450)

print(p1.get_price())
print(p2.get_price())

