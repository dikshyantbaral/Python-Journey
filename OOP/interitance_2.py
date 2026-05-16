#######Inheriting Constructor###if there is no contructor in child class when object is created then constructor of parent class will be called##
 class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class Smartphone(Phone):
    pass

s = Smartphone(20000, "Nokia", 13)
print(s.brand)





