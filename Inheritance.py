class students:
    def __init__ (self, name, age, total, grade):
        self.name= name
        self.age=age
        self.total=total
        self.grade= grade
    def display(self):
        print ("name:", self.name)
        print ("age:", self.age)
        print ("total:", self.total)
        print ("grade:", self.grade)
        print("_________________")
object=students("suresh", "23", "600", "A")
object2=students("rohith", "22", "555", "A")
object3=students("jensen", "23", 567, "A")
object.display()
object2.display()
object3.display()

print("-------------------------------------------")

class stddts:
    """ HELLO GUYS THIS IS MY FIRST OOPS CODE regarding students details"""
    def __init__ (self,name,dob,Rno,sec,total,age):
        self.name= name
        self.dob=dob
        self.Rno=Rno
        self.sec=sec
        self.total=total
        self.age=age
    def fun1(self):
        print ("Name ", self.name)
        print("DOB", self.dob)
        print("Roll Number", self.Rno)
        print("Section", self.sec)
        print("Total", self.total)
        print("Age", self.age)

obj=stddts("suresh", "20/4/1999", "16KD1A03A8", "A", 600, 23)
obj.fun1()
print(obj.__doc__)










