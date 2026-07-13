# Task 5. Abstraction(Using Abstract Base Class)
 
from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Credit Card Payment: {amount}")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"UPI Payment: {amount}")
c = CreditCardPayment()
u = UPIPayment()
c.process_payment(5000)
u.process_payment(10000)