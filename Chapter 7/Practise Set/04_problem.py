n = int(input("Enter a number: "))
i=0
c=0
for i in range(1,n+1):
       if (n%i==0):
           c+=1
if(c==2):
    print("The number is  prime ")
else:
    print("The number is not prime")