st = "Hey Dikshyant you are awesome"
f = open("myfile.txt","w")
f.write(st)
f.close()
f = open("myfile.txt","r")
data = f.read()
print(data)
f.close()