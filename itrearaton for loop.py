var=" india is my country"
for x in var:
    print("success")
    

var=" india is my country"
for x in var:
    print(x)
    print(x, end= "")
##    print(x, end="%")
##    
    
var="india is my country"
for x,y  in enumerate (var):
    print(x)
    print(y)

var=" india is my country"
##print (len(var))
my_counter=0
for x in var:
    my_counter=my_counter+1
    print(x)
print(my_counter)

var= "india is my country"
my_counter=0
for x in var:
    if x == "i":
        my_counter += 1
print("tatal i =", my_counter)

