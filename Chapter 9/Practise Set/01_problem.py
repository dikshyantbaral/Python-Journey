f = open("poems.txt")
c = f.read()
if("hello" in c):
    print("Twinkle is present")
else:
    print("Not present")
f.close()
