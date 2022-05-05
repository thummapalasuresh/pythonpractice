var= ["a", "b", "c"]
print (var)
print (type(var))

var1= ["a", 4, 5, 5.6]
print (var1)
print (type(var1))

var2=["a", 4.45, 5.6]
print (var2[0])

var[1]= "dhoni"
print (var)

bar= (1,2,3)
print (bar)
print (type(bar))
bar[2]= "subbarao"
print (bar)

bar1= ("a", "b", "c")
bar2= ("d", "e", "f")
bar3= (bar1+bar2)
print (bar3)

jar= ["a", "b"]
jar[0]= "dhani"
print (jar)
jar.insert(0, "dhoni")
print (jar)
jar[4]= "dhoni"
print(jar)
jar.insert(4, "dhoni")
print (jar)
jar.append("dhoni")
print (jar)
jar.append("dhoni", "kohli")
print (jar)
