a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))


if(a>b and a>c and a>d):
    print("a is the greatest:",a)
    
elif(b>a and b>c and b>d):
    print("b is the greatest:",b)
elif(c>b and c>a and c>d):
    print("c is the greatest:",c)
else:
    print("d is the greatest:",d)