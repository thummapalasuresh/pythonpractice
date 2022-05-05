fileobj=open("hello.txt", "w")
fileobj.write("welcome to python")
fileobj.close()

fileobj=open("hello.txt", "a")
fileobj.write("\n")
fileobj.write("welcome to myhome")
fileobj.close()

with open ("hello.txt", "a") as fileobj:
    fileobj.write("\n")
    fileobj.write("welcome to pyhon, this is my programm")

with open ("hello.txt", "r") as fileobj:
    data=fileobj.read()
    print (data)
    
with open ("hello.txt", "r") as fileobj:
    data=fileobj.readline()
    print (data)
    
with open ("hello.txt", "r") as fileobj:
    data=fileobj.readlines()
    print (data)
    
with open ("hello.txt", "r") as fileobj:
    data=fileobj.readline(10)
    print (data)
    data1=fileobj.readlines()
    print (data1)

with open ("hello.txt", "r") as fileobj:
    data=fileobj.readline(10)
    print (data)
    data1=fileobj.readlines()
    print (data1)
    print(len(data))
    print(len(data1))


with open ("hello.txt", "r") as fileobj:
    data=fileobj.read(100)
    print (data)
    data1=fileobj.read()
    print (data1)
    print(len(data))
    print(len(data1)) 



with open ("hello.txt", "a+") as fileobj:
    fileobj.write("\n")
    fileobj.write("welcome to chennai")
    fileobj.seek(0)
    data=fileobj.read()
    print(data)
    



with open ("hello.txt", "r+") as fileobj:
   
    data=fileobj.read()
    print(data)
    fileobj.write("\n")
    fileobj.write("welcome to chennai")


with open ("hello.txt", "a+") as fileobj:
    fileobj.write("\n")
    fileobj.write("welcome to chennai")
    fileobj.seek(0)
    data=fileobj.read
    print(data)
   


























