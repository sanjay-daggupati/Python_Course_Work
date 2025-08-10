from abc import ABC,abstractmethod 
"""class upload(ABC):
    @abstractmethod
    def compress(self):
        pass
    def edit(self):
        print("Edits are uploaded")
class Image(upload):
    def compress(self):
        print("Image is compressed to 2MB") 

class Reel(upload):
    def compress(self):
        print("Reel is compressed to 3MB")
#In abstraction for every child class we should have the same abstractmethod name  as in parentclass  
#In the above function only compress as abstract method so compress should be implemented in every child class 
#and we cannot have an instanace of abstract class
r=Reel()
i=Image()
r.compress()
i.compress()
r.edit()"""


"""
class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass 
class FoodOrder(Order):
    def process_order(self):
        print("Processing Food Order: check chef availabilty,estimate time")
class Groceryorder(Order):
    def process_order(self):
        print("Processin Grocery Order: Check inventory per item,")
class MedicineOrder(Order):
    def process_order(self):
        print("Processing Medicine Order: Validate prescription")
class CloudKitchenOrder(Order):
    def process_order(self):
        print("Processing Tiffen subscription: Schedule weekly delivers")
class PetSuppliesOrder(Order):
    def process_order(self):
        print("Processing Pet Supplies Order: Check Pet Product categories")
class MeatOrder(Order):
    def process_order(self):
        print("Processing Meat/SeaFood Order: Confirm Freshness")
class CakeOrder(Order):
    def process_order(self):
        print("Processing Cake Order: Custom Baking, time-senstive packaging")
class PartyOrder(Order):
    def process_order(self):
        print("Processing Party Order:Bulk Cooking,team Coordination")
class JuiceOrder(Order):
    def process_order(self):
        print("Processing Fresh Juice Order: Immediate prep,cold packaging")

def handle_order(order:Order):
    order.process_order()

orders=[
    FoodOrder(),
    Groceryorder(),
    MedicineOrder(),
    CloudKitchenOrder(),
    PetSuppliesOrder(),
    MeatOrder(),
    CakeOrder(),
    PartyOrder(),
    JuiceOrder()
]
for order in orders:
    handle_order(order)

order: Order means the parameter should be of type Order (or a subclass of Order) this is type hinting, not strict enforcement.
You are calling order.process_order(), assuming that whatever object is passed has a process_order() method.
Different classes can implement process_order() differently and that's polymorphism.
"""

class Payment(ABC):
    @abstractmethod
    def make_payment(self,amount):
        pass
class CreditCardPayment(ABC):
    def make_payment(self,amount):
        print(f"Paid ₹{amount} using Credit Card.")
class PayPalPayment(ABC):
    def make_payment(self,amount):
        print(f"Paid ₹{amount} via PayPal")
def process_payment(payment:Payment,amount):
    payment.make_payment(amount)

process_payment(CreditCardPayment(),100)
process_payment(PayPalPayment(),500)