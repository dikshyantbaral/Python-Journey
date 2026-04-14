class Customer:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
def greet(customer):
    if customer.gender == "Male":
        print("Hello", customer.name,"sir")
    else:
        print("Hello", customer.name,"mam")

 
        
cust = Customer("Nitesh","Male")
cust2 = Customer("Sumnima","Female")

greet(cust)
greet(cust2)
