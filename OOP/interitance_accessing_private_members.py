##Inheriting private members
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera

class Smartphone(Phone):
    pass

s = Smartphone(20000, "Nokia", 13)
print(s.__brand)


 
