##Polymorphism
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class Smartphone(Phone):
    def buy(self):
        print("Buying a smartphone")

s = Smartphone(20000, "Nokia", 13)
s.buy()


#Method overriding -> Polymorphism
# Method overloading
# Operator Overloading
