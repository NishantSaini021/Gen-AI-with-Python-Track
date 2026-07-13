# Magic Methods or Dunder Methods 
class Student:
    def __str__(self): #Triggered by print(obj) or str(obj)
        return "Nishant"

s = Student()

print(s)

#---------------------------------------------

class Book:
    def __len__(self): #Triggered by len(obj)
        return 500

b = Book()

print(len(b))

#---------------------------------------------

class Laptop:
    def __init__(self,brand): #Triggered when object is created
        self.brand = brand

    def __str__(self):
        return f"Laptop: {self.brand}"
l1 = Laptop("Dell")
print(l1)

#--------------------------------------------

class Laptop2:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Laptop: {self.brand}"
l2 = Laptop2("Dell")
print(l2)

# ---------------------------------------------

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"
    
    def __len__(self):
        return self.marks

s1 = Student("Nishant", 85)
print(s1)
print(len(s1))

# ---------------------------------------

class Student2:
    def __init__(self,marks):
        self.marks = marks


s2 = Student2(90)
s3 = Student2(90)
print(s3 == s2) #It will return false cause pyhton compares meomry address not marks
class Student3:
    def __init__(self,marks):
        self.marks = marks

    def __eq__(self,other):
        return self.marks == other.marks
s4 = Student3(96)
s5 = Student3(96)
print(s4 == s5)
#----------------------------------------
