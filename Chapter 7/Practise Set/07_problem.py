n = int(input("Enter a number: "))
for i in range(1,n+1):
 print(" "*(n-i),end="")#end = "", this doesnot give new line by default
 print("*"* (2*i-1), end="")
 print("")