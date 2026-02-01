a = int(input("Enter your age: "))
if(a%2==0):
    print("A is even")
    
if (a>=18):
    print("You can vote")
elif(a<0):
    print("Invalid Age!")
else:
    print("You cannot vote")
