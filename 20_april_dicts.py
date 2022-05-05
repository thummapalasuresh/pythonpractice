var = {"name":"dhoni","age":33}
for x in var:
    print(x)

var = {"name":"dhoni","age":33}
for x in var.items():
    print(x)

var = {"name":"dhoni","age":33}
for x in var.values():
    print(x)

var = {"name":"dhoni","age":33}
for key, value in var.items():
    print(key)
    print(value)


output = {0:0,1:1,2:4,3:9}

output = {}
for x in range(5):
    output[x] = x*x
print(output)

output= {x:x*x for x in range(5)}
print (output)

output= {x for x in range(10) if x%2==0}
print (output)

output= []
for x in range (10):
    if x%2==0:
        output.append(x)
print (output)

var=["dho", "asw", "fog"]
var.pop()
print (var)

var.pop(1)
print (var)


var.remove("dho")
print (var)


##var.remove(1)
##print (var)

var.clear()
print (var)

    



