# Operator overloading defines custom behaviour for standard operators
#  (+, -, *, ==, < etc.) on user-defined objects using magic methods.

class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

v1 = Vector(10)
v2 = Vector(20)

print(v1 + v2)

#-------------------------------------
class Vector:
    def __init__(self, x):
        self.x = x

    def __mul__(self, value):
        return self.x * value

v = Vector(5)

print(v * 3)

#--------------------------------------
class Vector:
    def __init__(self, x):
        self.x = x

    def __rmul__(self, value):# Value and X interchagne their position
        return self.x * value

v = Vector(10)

print(3 * v) 

# Operators like +, -, *, == are actually magic method calls behind the scenes.


class Money:
    def __init__(self,amount):
        self.amount = amount
    def __str__(self):
        return f"{self.amount}"
    def __add__(self,other):
        return self.amount + other.amount
m1 = Money(1000)
m2 = Money(500)
print(m1)
print(m1+m2)