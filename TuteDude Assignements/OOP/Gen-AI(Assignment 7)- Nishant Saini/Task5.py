# Task 5. Abstraction(Using Abstract Base Class)
 
from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(amount):
        pass
class CreditCardPayment(Payment):
    def process_payment(amount):
        print("Credit Card Payment")
class UPIPayment(Payment):
    def process_payment(amount):
        print("UPI Payment")
c = CreditCardPayment()
u = UPIPayment()
c.process_payment()
u.process_payment()