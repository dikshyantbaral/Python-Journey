class Customer:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print("I am",self.name, "and I am",self.age)
c1 = Customer("Nitish", 34)
c2 = Customer("Ankit",45)
c3 = Customer("Ankita",55)
c4 = Customer("Pulkit",35)

L = [c1,c2,c3,c4]

for i in L:
   # print(i.name,i.age)
    i.intro()
