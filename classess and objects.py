class myclass:
     def __init__(self, name):
         self.name= name
     def fun(self):
         print("hello", self.name)
     def _fun1(self):
         print("hi", self.name)
obj=myclass("dhoni")
obj.fun()
obj._fun1()  
 
