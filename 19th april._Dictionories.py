var={"dhoni",33}
print (var)
print (type(var))

var={"name":"suresh", "age": 33}
print (var)
print (type(var))

print (var["name"])
print (var[0])

var["name"]= "rajesh"
print (var)

var= {1: "dhoni", False:"kohli", 1.0:"ashwin"}
print(var[0])

var={"name":"suresh", "age": 33, 5.6:89, ("a", "b"): "suri" }
print (var)

var={"name":"suresh"} 
var2= {"age": 33}
print (var+var2)

var={"name":"suresh"} 
var2= {"age": 33}
var.update(var2)
print (var)

var={"name":"suresh"} 
var2= {"age": 33}
output= {**var, **var2}
print (output)

var={"name":"Kohli"}
var["country"]="india"
print(var)

var={"name":"Kohli", "country" : "india"}
print(var["age"])
print("welcome")

var={"name":"Kohli", "country" : "india"}
print(var.get("age","sorry"))
print("welcome")

var={"name":"Kohli", "country" : "india"}
print(var["country"])


