def convert(c):
    f = (1.8*c) + 32
    return f

c = int(input("Enter the value of celsius: "))
res = convert(c)
print(f"The fahrenheit value is: {round(res,3)}°C") #to print 3 decimals after it 